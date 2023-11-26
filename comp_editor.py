"""
CompEditor Application

This script defines a Tkinter-based GUI application for editing champion compositions.
"""

import tkinter as tk
from tkinter import ttk, simpledialog
import json
import os
import re
from comps import COMP
from game_assets import FULL_ITEMS, CHAMPIONS

CHAMPION_NAMES = list(CHAMPIONS.keys())
ITEM_OPTIONS = list(FULL_ITEMS.keys())


class CompEditor(tk.Tk):
    """
    Class representing the CompEditor application.

    Attributes:
        comp_tree (ttk.Treeview): Treeview widget for displaying champion details.
        COMP (dict): Dictionary containing champion data.
        trait_vars (list): List of StringVar instances for trait dropdowns.
    """

    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    def __init__(self, comp_data):
        super().__init__()

        self.title("Comp Editor")
        self.geometry("1280x720")

        self.comp_tree = ttk.Treeview(
            self, columns=("board_position", "level", "items", "traits", "final_comp")
        )
        self.comp_tree.heading("#0", text="Champion")
        self.comp_tree.heading("board_position", text="Board Position")
        self.comp_tree.heading("level", text="Level")
        self.comp_tree.heading("items", text="Items")
        self.comp_tree.heading("traits", text="Traits")
        self.comp_tree.heading("final_comp", text="Final Comp")
        self.comp_tree.grid(row=0, column=1, rowspan=8, sticky="nsew")

        self.comp = comp_data
        self.trait_vars = [tk.StringVar() for _ in range(3)]
        self.populate_tree()

        # Left side (Add Champion)
        left_frame = ttk.Frame(self)
        left_frame.grid(row=0, column=0, rowspan=8, padx=10, pady=10, sticky="nsew")

        self.champion_name_var = tk.StringVar(value=CHAMPION_NAMES[0])
        self.champion_dropdown = ttk.Combobox(
            left_frame, textvariable=self.champion_name_var, values=CHAMPION_NAMES
        )
        self.champion_dropdown.grid(
            row=0, column=0, columnspan=2, pady=5, padx=5, sticky="w"
        )
        self.champion_dropdown.bind(
            "<<ComboboxSelected>>", lambda event: self.update_traits_dropdowns()
        )

        self.board_position_var = tk.StringVar()
        self.create_label_entry(
            left_frame, "Board Position:", self.board_position_var, row=1
        )

        self.level_var = tk.StringVar()
        self.create_label_entry(left_frame, "Level:", self.level_var, row=2)

        self.item_dropdowns = []
        for i in range(3):
            item_var = tk.StringVar()
            item_label = f"Item {i+1}:"
            item_dropdown = ttk.Combobox(
                left_frame, textvariable=item_var, values=[""] + ITEM_OPTIONS
            )
            ttk.Label(left_frame, text=item_label).grid(
                row=i + 3, column=0, sticky="w", padx=5
            )
            item_dropdown.grid(row=i + 3, column=1, columnspan=2, pady=5, sticky="w")
            self.item_dropdowns.append(item_var)

        self.trait_dropdowns = self.create_trait_dropdowns(left_frame)
        self.update_traits_dropdowns()

        self.final_comp_var = tk.BooleanVar()
        self.create_checkbox(
            left_frame, "Final Composition:", self.final_comp_var, row=9
        )

        self.add_button = tk.Button(
            left_frame,
            text="Add Champion",
            command=self.add_champion,
            state=tk.DISABLED,
        )
        self.add_button.grid(row=10, column=0, columnspan=2, pady=10, sticky="w")

        # Right side (Remove Champion)
        remove_button = tk.Button(
            self, text="Remove Champion", command=self.remove_champion
        )
        remove_button.grid(row=8, column=1, sticky="e", pady=10, padx=10)

        # Save button
        save_button = tk.Button(self, text="Save", command=self.save_changes)
        save_button.grid(row=2, column=0, sticky="e", pady=10, padx=10)

        # Configure grid weights for resizing
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        left_frame.grid_columnconfigure(1, weight=1)
        left_frame.grid_rowconfigure(11, weight=1)

        # Bind the validation function to the variables
        self.champion_dropdown.bind(
            "<<ComboboxSelected>>", lambda event: self.update_traits_dropdowns()
        )
        self.board_position_var.trace_add("write", lambda *args: self.validate_inputs())
        self.level_var.trace_add("write", lambda *args: self.validate_inputs())
        self.comp_tree.bind("<Double-1>", lambda event: self.on_tree_double_click())

    def on_tree_double_click(self):
        """
        Handle double-click event on the Treeview widget.
        """
        selected_item = self.comp_tree.selection()
        if selected_item:
            champion = self.comp_tree.item(selected_item, "text")
            self.load_champion_details(champion)

    def load_champion_details(self, champion):
        """
        Load champion details into the input fields.
        """
        details = self.comp.get(champion)

        if details is None:
            print(f"Champion '{champion}' not found in comp.")
            return

        # Set champion name
        self.champion_name_var.set(champion)

        # Set other input fields
        self.board_position_var.set(details.get("board_position", ""))
        self.level_var.set(details.get("level", ""))
        self.final_comp_var.set(details.get("final_comp", ""))

        # Set item dropdowns
        for i, item_var in enumerate(self.item_dropdowns):
            items = details.get("items", [])
            if i < len(items):
                item_var.set(items[i])
            else:
                item_var.set("")

        # Update traits dropdowns based on the selected champion
        self.update_traits_dropdowns()

        # Set headliner traits
        headliner_traits = details.get("headliner", [])
        for i, (trait_var, trait_dropdown) in enumerate(
            zip(self.trait_vars, self.trait_dropdowns)
        ):
            if i < len(headliner_traits) and headliner_traits[i]:
                # Set trait only if headliner value is True
                trait_name = CHAMPIONS[champion].get(f"Trait{i + 1}", "")
                trait_var.set(trait_name)
                trait_dropdown.set(trait_name)
            else:
                trait_var.set("")
                trait_dropdown.set("")

    def create_trait_dropdown(self, frame, label_text, variable, row):
        """
        Create a single trait dropdown in the given frame.

        Args:
            frame (ttk.Frame): The frame in which to create the dropdown.
            label_text (str): The text for the dropdown label.
            variable: The variable associated with the dropdown.
            row (int): The row in which to place the dropdown.
        """
        trait_dropdown = ttk.Combobox(frame, textvariable=variable, values=[""])
        ttk.Label(frame, text=label_text).grid(row=row, column=0, sticky="w", padx=5)
        trait_dropdown.grid(row=row, column=1, columnspan=2, pady=5, sticky="w")
        return trait_dropdown

    def create_trait_dropdowns(self, frame):
        """
        Create trait dropdowns for the given champion.

        Args:
            frame (ttk.Frame): The frame in which to create the trait dropdowns.

        Returns:
            list: List of trait dropdowns.
        """
        trait_dropdowns = []
        for i in range(3):
            trait_var = tk.StringVar()
            trait_dropdown = self.create_trait_dropdown(
                frame, f"Trait {i + 1}:", trait_var, i + 6
            )
            trait_dropdowns.append(trait_dropdown)
        return trait_dropdowns

    def update_traits_dropdowns(self):
        """
        Update the traits dropdowns based on the selected champion.
        """
        selected_champion = self.champion_name_var.get()

        if selected_champion in CHAMPIONS:
            champion_traits = CHAMPIONS[selected_champion]
            traits = [
                champion_traits["Trait1"],
                champion_traits["Trait2"],
                champion_traits["Trait3"],
            ]
            num_traits = sum(1 for trait in traits if trait)
        else:
            traits = ["", "", ""]
            num_traits = 0

        filtered_traits = []
        seen_traits = set()

        for item in traits:
            if item and item not in seen_traits:
                filtered_traits.append(item)
                seen_traits.add(item)

        # Update the values in the dropdowns
        for i, (trait_var, trait_dropdown) in enumerate(
            zip(self.trait_vars, self.trait_dropdowns)
        ):
            trait_var.set("")  # Set the default choice to blank
            trait_dropdown["values"] = [""] + filtered_traits
            trait_dropdown.set("")

            # Disable dropdowns based on the number of available traits
            trait_dropdown["state"] = "normal"  # Reset state to normal
            if i >= num_traits:
                # Reset value to blank for disabled dropdowns
                trait_dropdown.set("")
                trait_dropdown["state"] = "disabled"

    def map_traits_to_headliner(self, selected_traits, champion_traits):
        """
        Map selected traits to positions in the headliner list.

        Args:
            selected_traits (list): List of selected traits by the user.
            champion_traits (list): List of traits associated with the selected champion.

        Returns:
            list: A list representing the headliner with True at positions corresponding to selected traits.
        """
        headliner = [False] * 3
        for trait in selected_traits:
            if trait in champion_traits and trait != "":
                headliner[champion_traits.index(trait)] = True
        return headliner

    def create_label_entry(self, frame, label_text, variable, row=None):
        """
        Create a label and entry widget pair in the given frame.

        Args:
            frame (ttk.Frame): The frame in which to create the widgets.
            label_text (str): The text for the label widget.
            variable: The variable associated with the entry widget.
            var_type: The type of variable to create (default is tk.StringVar).
            row (int): The row in which to place the widgets.
        """
        ttk.Label(frame, text=label_text).grid(row=row, column=0, sticky="w", padx=5)
        tk.Entry(frame, textvariable=variable).grid(
            row=row, column=1, sticky="w", padx=5
        )

    def create_checkbox(self, frame, label_text, variable, row=None):
        """
        Create a checkbox widget in the given frame.

        Args:
            frame (ttk.Frame): The frame in which to create the checkbox.
            label_text (str): The text for the checkbox.
            variable: The variable associated with the checkbox.
            row (int): The row in which to place the checkbox.
        """
        checkbox = ttk.Checkbutton(frame, text=label_text, variable=variable)
        checkbox.grid(row=row, column=1, pady=5, sticky="e")

    def populate_tree(self):
        """
        Populate the Treeview widget with champion data.
        """
        for champion, details in sorted(
            self.comp.items(), key=lambda x: x[1]["board_position"]
        ):
            # Fetch traits from CHAMPIONS
            champion_data = CHAMPIONS.get(champion, {})
            traits = [champion_data.get(f"Trait{i+1}", "") for i in range(3)]

            # Update traits based on headliner values
            headliner_values = details.get("headliner", [False, False, False])
            traits = [
                trait if headliner else ""
                for trait, headliner in zip(traits, headliner_values)
            ]

            filtered_traits = []
            seen_traits = set()

            for item in traits:
                if item and item not in seen_traits:
                    filtered_traits.append(item)
                    seen_traits.add(item)

            self.comp_tree.insert(
                "",
                "end",
                text=champion,
                values=(
                    details["board_position"],
                    details["level"],
                    ", ".join(details["items"]),
                    ", ".join(filtered_traits),
                    details["final_comp"],
                ),
            )

    def validate_inputs(self):
        """
        Validate user inputs for adding a champion.
        """
        champion_selected = self.champion_name_var.get()
        board_position_str = self.board_position_var.get()
        level_str = self.level_var.get()

        if (
            champion_selected
            and self.is_valid_board_position_str(board_position_str)
            and self.is_valid_level_str(level_str)
        ):
            self.add_button["state"] = tk.NORMAL
        else:
            self.add_button["state"] = tk.DISABLED

    def is_valid_board_position_str(self, board_position_str):
        """
        Check if the board position string is valid.

        Args:
            board_position_str (str): The string to check.

        Returns:
            bool: True if the string is a valid board position, False otherwise.
        """
        try:
            board_position = int(board_position_str)
            return self.is_valid_board_position(board_position)
        except ValueError:
            return False

    def is_valid_board_position(self, board_position):
        """
        Check if the board position is valid.

        Args:
            board_position (int): The board position to check.

        Returns:
            bool: True if the board position is valid, False otherwise.
        """
        selected_champion = self.champion_name_var.get()

        # Exclude the currently chosen champion from the check
        champions_to_check = {
            name: champion["board_position"]
            for name, champion in self.comp.items()
            if name != selected_champion
        }

        return 0 <= board_position <= 27 and not any(
            position == board_position for position in champions_to_check.values()
        )

    def is_valid_level_str(self, level_str):
        """
        Check if the level string is valid.

        Args:
            level_str (str): The string to check.

        Returns:
            bool: True if the string is a valid level, False otherwise.
        """
        try:
            level = int(level_str)
            return self.is_valid_level(level)
        except ValueError:
            return False

    def is_valid_level(self, level):
        """
        Check if the level is valid.

        Args:
            level (int): The level to check.

        Returns:
            bool: True if the level is valid, False otherwise.
        """
        return level in {1, 2, 3}

    def add_champion(self):
        """
        Add a new champion based on user inputs.

        Retrieves information entered by the user, validates it,
        and then adds a new champion to the COMP data structure.
        """
        board_position = self.validate_board_position()
        items = self.validate_and_filter_items()
        level = self.validate_level()
        final_comp = self.final_comp_var.get()
        selected_traits = self.get_selected_traits()
        selected_champion = self.champion_name_var.get()

        if selected_champion in CHAMPIONS:
            champion_traits = CHAMPIONS[selected_champion]
            traits = [champion_traits[f"Trait{i+1}"] for i in range(3)]
        else:
            traits = ["", "", ""]

        headliner = self.map_traits_to_headliner(selected_traits, traits)

        new_champion = {
            "board_position": board_position,
            "level": level,
            "items": items,
            "traits": selected_traits,
            "final_comp": final_comp,
            "headliner": headliner,
        }

        self.comp[selected_champion] = new_champion
        self.comp_tree.delete(*self.comp_tree.get_children())
        self.populate_tree()

    def validate_board_position(self):
        """
        Validate and retrieve the board position entered by the user.

        Returns:
            int or None: The validated board position or None if validation fails.
        """
        board_position_str = self.board_position_var.get()
        try:
            board_position = int(board_position_str)
            if not self.is_valid_board_position(board_position):
                simpledialog.messagebox.showerror(
                    "Error",
                    "Board Position must be a valid number between 0 and 27 and not already taken.",
                )
                return None
            return board_position
        except ValueError:
            simpledialog.messagebox.showerror(
                "Error", "Board Position must be a valid number."
            )
            return None

    def validate_and_filter_items(self):
        """
        Validate and filter the selected items entered by the user.

        Returns:
            list or None: The filtered list of items or None if validation fails.
        """
        items_selected = [item_var.get() for item_var in self.item_dropdowns]
        filtered_items = list(filter(lambda item: item, items_selected))
        if not all(self.is_valid_item(item) for item in items_selected):
            simpledialog.messagebox.showerror(
                "Error", "Items can only contain letters (a-zA-Z) and commas."
            )
            return None
        return filtered_items

    def validate_level(self):
        """
        Validate and retrieve the level entered by the user.

        Returns:
            int or None: The validated level or None if validation fails.
        """
        level_str = self.level_var.get()
        if not self.is_valid_level_str(level_str):
            simpledialog.messagebox.showerror(
                "Error", "Level must be a valid number between 1 and 3."
            )
            return None
        return int(level_str)

    def get_selected_traits(self):
        """
        Retrieve and filter the selected traits entered by the user.

        Returns:
            list: The filtered list of selected traits.
        """
        selected_traits = [trait_var.get() for trait_var in self.trait_dropdowns]
        filtered_traits = []
        seen_traits = set()

        for item in selected_traits:
            if item and item not in seen_traits:
                filtered_traits.append(item)
                seen_traits.add(item)

        return filtered_traits

    def is_valid_item(self, item):
        """
        Check if the item string is valid.

        Args:
            item (str): The item string to check.

        Returns:
            bool: True if the item string is valid, False otherwise.
        """
        return all(c.isalpha() or c.isnumeric() or c == "," for c in item)

    def remove_champion(self):
        """
        Remove the selected champion from the Treeview and data.
        """
        selected_item = self.comp_tree.selection()
        if selected_item:
            champion = self.comp_tree.item(selected_item, "text")
            del self.comp[champion]
            self.comp_tree.delete(selected_item)

    def save_changes(self):
        """
        Save changes made in the application to the comps.py file.
        """
        current_file_path = os.path.abspath(__file__)
        comps_file_path = os.path.join(os.path.dirname(current_file_path), "comps.py")

        with open(comps_file_path, "r", encoding="utf-8", newline='') as file:
            file_content = file.read()

        comp_line_start = file_content.find("COMP = {")
        if comp_line_start == -1:
            print("Error: COMP variable not found in the file.")
            return

        comp_line_end = comp_line_start
        brace_count = 0

        for _, char in enumerate(file_content[comp_line_start:], start=1):
            comp_line_end += 1

            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1

            if brace_count == 0 and char == "}":
                break

        updated_file_content = (
            file_content[:comp_line_start]
            + "COMP = "
            + re.sub(
                r'"traits": \[.*?\],\n?',
                "",
                json.dumps(self.comp, indent=4),
                flags=re.DOTALL,
            )
            .replace("false", "False")
            .replace("true", "True")
            .replace("                ", "        ")
            .replace("\n           ", "")
            .replace("\n        ]", "]")
            .replace("\r           ", "")
            .replace("\r        ]", "]")
            .replace("[ ", "[")
            .replace("\r\n",'\n')
            + file_content[comp_line_end:]
        )

        with open(comps_file_path, "w", encoding="utf-8", newline='') as file:
            file.write(updated_file_content)


if __name__ == "__main__":
    app = CompEditor(COMP)
    app.mainloop()
