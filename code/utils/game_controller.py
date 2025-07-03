import os
from world.location import Location
from world.droid import DamagedMaintenanceDroid
from items.diagnostic_tool import DiagnosticTool
from items.energy_crystal import EnergyCrystal
from player.player import Player

class GameController:
    def __init__(self):
        self.maintenance_tunnels = None
        self.docking_bay = None
        self.droid = None
        self.diagnostic_tool = None
        self.energy_crystal = None
        self.player = None
        self.last_command = ""
        self.commands = [
            "move <direction> - Move to another location",
            "pick up tool - Pick up the diagnostic tool",
            "use tool - Use the tool on the droid",
            "pick up crystal - Pick up the energy crystal",
            "status - Show your current score and hazards",
            "win - Complete the mission"
        ]

        self.setup_world()

    def setup_world(self):
        self.maintenance_tunnels = Location("Maintenance Tunnels", "Dimly lit corridors echo with mechanical humming.")
        self.docking_bay = Location("Docking Bay", "A large, open bay with glowing panels.")

        self.maintenance_tunnels.has_tool = True
        self.maintenance_tunnels.droid_present = True
        self.docking_bay.has_crystal = True

        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)

        self.droid = DamagedMaintenanceDroid()
        self.diagnostic_tool = DiagnosticTool()
        self.energy_crystal = EnergyCrystal()

        self.player = Player(self.maintenance_tunnels)

    def clear_screen(self, show_welcome=False):
        """Clear the screen and display available commands.
        
        Args:
            show_welcome (bool): Whether to show the welcome message
        """
        # Clear screen based on OS
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if show_welcome:
            print("Welcome to the Maintenance Mission!")
            print()
        
        print("Available Commands:")
        for cmd in self.commands:
            print(f"- {cmd}")
        print()

    def start_game(self):
        # Clear screen and show initial location
        self.clear_screen()
        print(self.player.current_location.describe())
        
        while True:
            command = input("> ").strip().lower()
            self.last_command = command
            self.process_input(command)
            if self.check_win_condition():
                break

    def process_input(self, command):
        if command.startswith("move"):
            # Split the command to get direction
            parts = command.split()
            if len(parts) < 2:
                print("Please specify a direction to move (e.g., 'move east')")
                return
            
            direction = parts[1]
            success, message = self.player.move(direction)
            print(message)
        elif command == "pick up tool":
            success, message = self.player.pick_up_tool()
            print(message)
        elif command == "use tool":
            success, message = self.player.use_tool_on_droid(self.droid)
            print(message)
        elif command == "pick up crystal":
            success, message = self.player.pick_up_crystal()
            print(message)
        elif command == "status":
            print(self.player.get_status())
        elif command == "win":
            if self.check_win_condition():
                return True
            print("You must be in the Docking Bay with the crystal to win.")
        else:
            print("Invalid command.")

    def check_win_condition(self):
        if (self.player.current_location == self.docking_bay and
            self.player.has_crystal and
            self.last_command == "win"):
            self.player.score += 30
            print(f"Mission complete! Final Score: {self.player.score} Total Hazards: {self.player.hazard_count}")
            return True
        return False
