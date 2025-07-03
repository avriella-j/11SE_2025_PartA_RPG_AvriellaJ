# Space Station RPG

A text-based RPG game set in a space station, developed as part of Year 11 Software Engineering.

## Game Overview

The player must follow a fixed "golden path" and earn points exactly as described below. If the player tries to move past the droid before it is repaired, a hazard counter increases. At the end, the game displays total score and hazards.

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
code/
├── __init__.py
├── utils/
│   ├── __init__.py
│   └── game_controller.py
├── items/
│   ├── __init__.py
│   ├── diagnostic_tool.py
│   └── energy_crystal.py
├── player/
│   ├── __init__.py
│   └── player.py
└── world/
    ├── __init__.py
    ├── location.py
    └── droid.py
```

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python code/main.py
```

## Features

- Space station exploration
- Item collection and usage
- NPC interactions
- Location-based puzzles
- Inventory management
