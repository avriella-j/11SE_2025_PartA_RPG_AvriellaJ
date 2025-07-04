# Space Station RPG

A text-based RPG game set in a space station. Players must navigate through the station, collect items, and solve puzzles while managing hazards.

## Game Overview

### Storyline
The space station's maintenance droid has malfunctioned, causing critical systems to fail. Players must repair the droid and retrieve the energy crystal to restore power to the station.

### Objective
Complete the mission by:
1. Repairing the maintenance droid
2. Collecting the energy crystal
3. Returning to the docking bay

### Game Mechanics
- Text-based navigation using cardinal directions (north, south, east, west)
- Item collection and usage
- NPC interactions
- Hazard management
- Score tracking

### Scoring System
- Points awarded for completing tasks
- Hazards reduce final score
- Bonus points for completing mission objectives

### Golden Path Steps (in order):

1. **Maintenance Tunnels**: Player begins here.
2. **Pick up the Diagnostic Tool** (awards +10 points).
3. **Use the Diagnostic Tool on the Damaged Maintenance Droid** (awards +20 points) to clear it.
4. **Move to Docking Bay**.
5. **Pick up the Energy Crystal** (awards +50 points).
6. **Type "win"** (from Docking Bay) to complete the mission (awards +30 points).

### Hazard Rule:

If the player tries to move east (toward Docking Bay) while the droid is still blocking, increment the hazard counter by 1 and display a "droid blocking" message.

## Project Structure

```
11SE_2025_PartA_RPG_AvriellaJ/
├── code/
│   ├── __init__.py
│   ├── main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── game_controller.py
│   ├── items/
│   │   ├── __init__.py
│   │   ├── diagnostic_tool.py
│   │   └── energy_crystal.py
│   ├── player/
│   │   ├── __init__.py
│   │   └── player.py
│   └── world/
│       ├── __init__.py
│       ├── location.py
│       └── droid.py
├── docs/
│   └── CHANGELOG.md
├── logs/
│   └── game.log
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Game
1. Navigate to the project directory
2. Execute the main game file:
```bash
python code/main.py
```

### Game Controls
- Use cardinal directions (north, south, east, west) to navigate
- Type "inventory" to view current items
- Type "help" for available commands
- Type "quit" to exit the game

## Features

### Core Features
- Interactive text-based gameplay
- Dynamic inventory system
- Location-based puzzles and challenges
- NPC interactions and dialogue
- Score tracking and hazard management

### Technical Features
- Object-oriented design
- Modular code structure
- Automated logging system
- Comprehensive documentation
- Error handling and validation
