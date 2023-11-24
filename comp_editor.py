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

    def __init__(self, comp_data):
        super().__init__()

        self.title("Comp Editor")
        self.geometry("1280x720")

        self.comp_tree = ttk.Treeview(self, columns=(
            "board_position", "level", "items", "traits", "final_comp"))
        self.comp_tree.heading("#0", text="Champion")
        self.comp_tree.heading("board_position", text="Board Position")
        self.comp_tree.heading("level", text="Level")
        self.comp_tree.heading("items", text="Items")
        self.comp_tree.heading("traits", text="Traits")
        self.comp_tree.heading("final_comp", text="Final Comp")
        self.comp_tree.grid(row=0, column=1, rowspan=8, sticky="nsew")

        self.COMP = comp_data
        self.trait_vars = [tk.StringVar() for _ in range(3)]
        self.populate_tree()

        # Left side (Add Champion)
        left_frame = ttk.Frame(self)
        left_frame.grid(row=0, column=0, rowspan=8,
                        padx=10, pady=10, sticky="nsew")

        self.champion_name_var = tk.StringVar(value=CHAMPION_NAMES[0])
        self.champion_dropdown = ttk.Combobox(
            left_frame, textvariable=self.champion_name_var, values=CHAMPION_NAMES)
        self.champion_dropdown.grid(
            row=0, column=0, columnspan=2, pady=5, padx=5, sticky="w")
        self.champion_dropdown.bind(
            "<<ComboboxSelected>>", lambda event: self.update_traits_dropdowns())

        self.board_position_var = tk.StringVar()
        self.create_label_entry(
            left_frame, "Board Position:", self.board_position_var, tk.IntVar, row=1)

        self.level_var = tk.StringVar()
        self.create_label_entry(left_frame, "Level:",
                                self.level_var, tk.IntVar, row=2)

        self.item_dropdowns = []
        for i in range(3):
            item_var = tk.StringVar()
            item_label = f"Item {i+1}:"
            item_dropdown = ttk.Combobox(
                left_frame, textvariable=item_var, values=[""] + ITEM_OPTIONS)
            ttk.Label(left_frame, text=item_label).grid(
                row=i + 3, column=0, sticky="w", padx=5)
            item_dropdown.grid(row=i + 3, column=1,
                               columnspan=2, pady=5, sticky="w")
            self.item_dropdowns.append(item_var)

        self.trait_dropdowns = self.create_trait_dropdowns(
            left_frame, self.champion_name_var.get())
        self.update_traits_dropdowns()

        self.final_comp_var = tk.BooleanVar()
        self.create_checkbox(left_frame, "Final Composition:",
                             self.final_comp_var, row=9)

        self.add_button = tk.Button(
            left_frame, text="Add Champion", command=self.add_champion, state=tk.DISABLED)
        self.add_button.grid(
            row=10, column=0, columnspan=2, pady=10, sticky="w")

        # Right side (Remove Champion)
        remove_button = tk.Button(
            self, text="Remove Champion", command=self.remove_champion)
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
            "<<ComboboxSelected>>", lambda event: self.update_traits_dropdowns())
        self.board_position_var.trace_add(
            "write", lambda *args: self.validate_inputs())
        self.level_var.trace_add("write", lambda *args: self.validate_inputs())

    def create_trait_dropdowns(self, frame, champion_name):
        """
        Create trait dropdowns for the given champion.

        Args:
            frame (ttk.Frame): The frame in which to create the trait dropdowns.
            champion_name (str): The name of the selected champion.

        Returns:
            list: List of trait dropdowns.
        """
        trait_dropdowns = []
        for i in range(3):
            trait_var = tk.StringVar()
            trait_dropdown = ttk.Combobox(
                frame, textvariable=trait_var, values=[""])
            ttk.Label(
                frame, text=f"Trait {i + 1}:").grid(row=i + 6, column=0, sticky="w", padx=5)
            trait_dropdown.grid(row=i + 6, column=1,
                                columnspan=2, pady=5, sticky="w")
            trait_dropdowns.append(trait_dropdown)
        return trait_dropdowns

    def update_traits_dropdowns(self, *args):
        """
        Update the traits dropdowns based on the selected champion.
        """
        selected_champion = self.champion_name_var.get()

        if selected_champion in CHAMPIONS:
            champion_traits = CHAMPIONS[selected_champion]
            traits = [champion_traits["Trait1"],
                      champion_traits["Trait2"], champion_traits["Trait3"]]
        else:
            traits = ["", "", ""]

        # Update the values in the dropdowns
        for i, (trait_var, trait_dropdown) in enumerate(zip(self.trait_vars, self.trait_dropdowns)):
            trait_var.set(traits[i])
            trait_dropdown['values'] = [""] + traits
            trait_dropdown.set(traits[i])

    def create_label_entry(self, frame, label_text, variable, var_type=tk.StringVar, row=None):
        """
        Create a label and entry widget pair in the given frame.

        Args:
            frame (ttk.Frame): The frame in which to create the widgets.
            label_text (str): The text for the label widget.
            variable: The variable associated with the entry widget.
            var_type: The type of variable to create (default is tk.StringVar).
            row (int): The row in which to place the widgets.
        """
        ttk.Label(frame, text=label_text).grid(
            row=row, column=0, sticky="w", padx=5)
        tk.Entry(frame, textvariable=variable).grid(
            row=row, column=1, sticky="w", padx=5)

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
        for champion, details in sorted(self.COMP.items(), key=lambda x: x[1]["board_position"]):
            self.comp_tree.insert("", "end", text=champion, values=(
                details["board_position"],
                details["level"],
                ", ".join(details["items"]),
                ", ".join(details.get("traits", [])),
                details["final_comp"]
            ))

    def validate_inputs(self):
        """
        Validate user inputs for adding a champion.
        """
        champion_selected = self.champion_name_var.get()
        board_position_str = self.board_position_var.get()
        level_str = self.level_var.get()

        if (
            champion_selected and
            self.is_valid_board_position_str(board_position_str) and
            self.is_valid_level_str(level_str)
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
        return 0 <= board_position <= 27 and not any(champion["board_position"] == board_position for champion in self.COMP.values())

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
        """
        board_position_str = self.board_position_var.get()
        try:
            board_position = int(board_position_str)
            if not self.is_valid_board_position(board_position):
                simpledialog.messagebox.showerror(
                    "Error", "Board Position must be a valid number between 0 and 27 and not already taken.")
                return
        except ValueError:
            simpledialog.messagebox.showerror(
                "Error", "Board Position must be a valid number.")
            return

        items_selected = [item_var.get() for item_var in self.item_dropdowns]
        filtered_items = list(filter(lambda item: item, items_selected))
        if not all(self.is_valid_item(item) for item in items_selected):
            simpledialog.messagebox.showerror(
                "Error", "Items can only contain letters (a-zA-Z) and commas.")
            return

        level_str = self.level_var.get()
        if not self.is_valid_level_str(level_str):
            simpledialog.messagebox.showerror(
                "Error", "Level must be a valid number between 1 and 3.")
            return

        final_comp = self.final_comp_var.get()

        selected_traits = [trait_var.get()
                           for trait_var in self.trait_dropdowns]
        filtered_traits = []
        seen_traits = set()

        for item in selected_traits:
            if item and item not in seen_traits:
                filtered_traits.append(item)
                seen_traits.add(item)

        new_champion = {
            "board_position": int(board_position_str),
            "level": int(level_str),
            "items": filtered_items,
            "traits": filtered_traits,
            "final_comp": final_comp
        }

        self.COMP[self.champion_name_var.get()] = new_champion
        self.comp_tree.delete(*self.comp_tree.get_children())
        self.populate_tree()

    def is_valid_item(self, item):
        """
        Check if the item string is valid.

        Args:
            item (str): The item string to check.

        Returns:
            bool: True if the item string is valid, False otherwise.
        """
        return all(c.isalpha() or c.isnumeric() or c == ',' for c in item)

    def remove_champion(self):
        """
        Remove the selected champion from the Treeview and data.
        """
        selected_item = self.comp_tree.selection()
        if selected_item:
            champion = self.comp_tree.item(selected_item, "text")
            del self.COMP[champion]
            self.comp_tree.delete(selected_item)

    def save_changes(self):
        """
        Save changes made in the application to the comps.py file.
        """
        current_file_path = os.path.abspath(__file__)
        comps_file_path = os.path.join(
            os.path.dirname(current_file_path), "comps.py")

        updated_comp_str = json.dumps(self.COMP, indent=4)

        with open(comps_file_path, "r") as file:
            file_content = file.read()

        comp_line_start = file_content.find("COMP = {")
        if comp_line_start == -1:
            print("Error: COMP variable not found in the file.")
            return

        comp_line_end = comp_line_start
        brace_count = 0

        for line_number, char in enumerate(file_content[comp_line_start:], start=1):
            comp_line_end += 1

            if char == "{":
                brace_count += 1
            elif char == "}":
                brace_count -= 1

            if brace_count == 0 and char == "}":
                break

        updated_file_content = (
            file_content[:comp_line_start] +
            "COMP = " + updated_comp_str +
            file_content[comp_line_end:]
        )

        with open(comps_file_path, "w") as file:
            file.write(updated_file_content)

        with open(comps_file_path, "r") as file:
            file_content = file.read()

        updated_content = file_content.replace(
            "false", "False").replace("true", "True")

        with open(comps_file_path, "w") as file:
            file.write(updated_content)


if __name__ == "__main__":
    app = CompEditor(COMP)
    app.mainloop()
