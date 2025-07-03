import logging
from datetime import datetime
from pathlib import Path

class GameLogger:
    """Logger class for the Space Station RPG game.
    
    This class provides logging functionality for game events, player actions,
    and debugging information. Logs are saved to a file and can be configured
    to different levels of detail.
    """
    
    def __init__(self, log_file: str = "game.log"):
        """Initialise the GameLogger.
        
        Args:
            log_file (str): Path to the log file. Defaults to "game.log".
        """
        # Create logs directory if it doesn't exist
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)
        
        # Set up logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(logs_dir / log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("SpaceStationRPG")
        
    def log_game_event(self, message, level="INFO"):
        """Log a game event.
        
        Args:
            message (str): The message to log
            level (str): The log level (INFO, WARNING, ERROR, DEBUG)
        """
        level = level.upper()
        if level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "DEBUG":
            self.logger.debug(message)
        else:
            self.logger.error(f"Invalid log level: {level}")
            self.logger.info(message)

    def log_player_action(self, player_name, action, location):
        """Log a player's action.
        
        Args:
            player_name (str): Name of the player
            action (str): Action performed
            location (str): Location where action occurred
        """
        message = f"Player {player_name} performed action '{action}' in {location}"
        self.log_game_event(message)

    def log_item_interaction(self, player_name, item_name, action):
        """Log an interaction with an item.
        
        Args:
            player_name (str): Name of the player
            item_name (str): Name of the item
            action (str): Action performed with the item
        """
        message = f"Player {player_name} {action} {item_name}"
        self.log_game_event(message)

    def log_npc_interaction(self, player_name, npc_name, action):
        """Log an interaction with an NPC.
        
        Args:
            player_name (str): Name of the player
            npc_name (str): Name of the NPC
            action (str): Action performed
        """
        message = f"Player {player_name} interacted with {npc_name}: {action}"
        self.log_game_event(message)

    def set_log_level(self, level):
        """Set the logging level.
        
        Args:
            level (str): Log level (INFO, WARNING, ERROR, DEBUG)
        """
        level = level.upper()
        if level in ["INFO", "WARNING", "ERROR", "DEBUG"]:
            self.logger.setLevel(level)
        else:
            self.logger.error(f"Invalid log level: {level}")
            self.logger.setLevel("INFO")

    def get_log_level(self):
        """Get the current log level.
        
        Returns:
            str: Current log level
        """
        return logging.getLevelName(self.logger.level)
