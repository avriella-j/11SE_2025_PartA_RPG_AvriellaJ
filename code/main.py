from utils.game_controller import GameController
import os

def main():
    # Clear screen and show welcome message
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Maintenance Mission!")
    print("\nAvailable Commands:")
    print("- move <direction> - Move to another location")
    print("- pick up tool - Pick up the diagnostic tool")
    print("- use tool - Use the tool on the droid")
    print("- pick up crystal - Pick up the energy crystal")
    print("- status - Show your current score and hazards")
    print("- win - Complete the mission")
    print()
    input("\nPress Enter to begin your mission...")
    print()
    
    # Start the game
    game = GameController()
    game.start_game()

if __name__ == "__main__":
    main()
