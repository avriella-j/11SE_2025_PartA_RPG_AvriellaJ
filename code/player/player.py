class Player:
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.has_tool = False
        self.has_crystal = False
        self.score = 0
        self.hazard_count = 0

    def move(self, direction):
        direction = direction.lower()

        if direction not in self.current_location.exits:
            return False, "You can't go that way."

        if self.current_location.droid_present:
            self.hazard_count += 1
            return False, "A maintenance droid blocks your path!"

        self.current_location = self.current_location.exits[direction]
        return True, f"You move {direction} to {self.current_location.name}."

    def pick_up_tool(self):
        success, message = self.current_location.remove_tool()
        if success:
            self.has_tool = True
            self.score += 10
        return success, message

    def use_tool_on_droid(self, droid=None):
        if droid is None:
            return False, "No droid found to repair."
        
        if self.has_tool and self.current_location.droid_present and droid.is_blocking():
            droid.repair()
            self.current_location.set_droid_present(False)
            self.score += 20
            return True, "You used the tool to repair the droid. It powers down silently."
        return False, "Nothing happens."

    def pick_up_crystal(self):
        success, message = self.current_location.remove_crystal()
        if success:
            self.has_crystal = True
            self.score += 50
        return success, message

    def get_status(self):
        return f"Score: {self.score} | Hazards encountered: {self.hazard_count}"
