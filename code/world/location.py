class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits: dict[str, 'Location'] = {}
        self.has_tool = False
        self.has_crystal = False
        self.droid_present = False

    def add_exit(self, direction, other_location):
        self.exits[direction.lower()] = other_location

    def describe(self):
        lines = [f"\n== {self.name} ==\n{self.description}\n"]

        if self.has_tool:
            lines.append("You see a diagnostic tool here.")
        if self.has_crystal:
            lines.append("You see an energy crystal here.")
        if self.droid_present:
            lines.append("A maintenence droid blocks the way!")
        
        if self.exits:
            exits_list = ", ".join(self.exits.keys())
            lines.append(f"Exits: {exits_list}.")
        else:
            lines.append("There are no visible exits.")

        return "\n".join(lines)

    def remove_tool(self):
        if self.has_tool:
            self.has_tool = False
            return True, "You take the tool."
        return False, "There is no tool to pick up."

    def remove_crystal(self):
        if self.has_crystal:
            self.has_crystal = False
            return True, "You take the energy crystal."
        return False, "There is no crystal to pick up."

    def set_droid_present(self, flag):
        self.droid_present = flag