"""
CompEditor Application

This script defines a Tkinter-based GUI application for editing champion compositions.
"""

import tkinter as tk
from tkinter import ttk, simpledialog
import json
import os
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
            self, columns=("board_position", "level", "items", "final_comp")
        )
        self.comp_tree.heading("#0", text="Champion")
        self.comp_tree.heading("board_position", text="Board Position")
        self.comp_tree.heading("level", text="Level")
        self.comp_tree.heading("items", text="Items")
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
            self.comp_tree.insert(
                "",
                "end",
                text=champion,
                values=(
                    details["board_position"],
                    details["level"],
                    ", ".join(details["items"]),
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
        selected_champion = self.champion_name_var.get()

        new_champion = {
            "board_position": board_position,
            "items": items,
            "level": level,
            "final_comp": final_comp,
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
            + json.dumps(self.comp, indent=4)
            .replace("false", "False")
            .replace("true", "True")
            .replace("                ", "        ")
            .replace("\n           ", "")
            .replace("\n        ]", "]")
            .replace("[ ", "[")
            + file_content[comp_line_end:]
        )

        with open(comps_file_path, "w", encoding="utf-8", newline='') as file:
            file.write(updated_file_content)


if __name__ == "__main__":
    app = CompEditor(COMP)
    app.mainloop()
