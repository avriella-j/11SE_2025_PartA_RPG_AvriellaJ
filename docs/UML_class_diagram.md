# 📊 UML Class Diagram — RPG Game

## 🧩 Class: `StationItem` (Abstract Base Class)
**Attributes**:
- `_name`
- `_description`

**Methods**:
- `examine()` → Returns a description (overridden by subclasses)

---

## 🔧 Class: `DiagnosticTool` (inherits from `StationItem`)
**Methods**:
- `examine()` → Returns a diagnostic hint

---

## 💎 Class: `EnergyCrystal` (inherits from `StationItem`)
**Methods**:
- `examine()` → Returns a crystal-specific description

---

## 🌍 Class: `Location`
**Attributes**:
- `name`
- `description`
- `exits` *(dictionary of direction → Location)*
- `has_tool` *(bool)*
- `has_crystal` *(bool)*
- `droid_present` *(bool)*

**Methods**:
- `__init__()`
- `add_exit(direction, location)`
- `describe()`
- `remove_tool()`
- `remove_crystal()`
- `set_droid_present(flag)`

---

## 🤖 Class: `DamagedMaintenanceDroid`
**Attributes**:
- `blocking` *(bool)*

**Methods**:
- `__init__()` → Sets blocking to True
- `repair()` → Sets blocking to False
- `is_blocking()` → Returns blocking status

---

## 🧍 Class: `Player`
**Attributes**:
- `current_location` *(Location)*
- `has_tool` *(bool)*
- `has_crystal` *(bool)*
- `score` *(int)*
- `hazard_count` *(int)*

**Methods**:
- `__init__(starting_location)`
- `move(direction)`
- `pick_up_tool()`
- `use_tool_on_droid()`
- `pick_up_crystal()`
- `get_status()`

---

## 🎮 Class: `GameController`
**Attributes**:
- `maintenance_tunnels` *(Location)*
- `docking_bay` *(Location)*
- `droid` *(DamagedMaintenanceDroid)*
- `player` *(Player)*
- `diagnostic_tool` *(DiagnosticTool)*
- `energy_crystal` *(EnergyCrystal)*

**Methods**:
- `__init__()`
- `setup_world()`
- `start_game()`
- `process_input(cmd)`
- `check_win_condition()`

---

## 🔗 Class Relationships

- `DiagnosticTool` and `EnergyCrystal` → Inherit from `StationItem`
- `Location` → Contains one or more:
  - Tool
  - Crystal
  - DamagedMaintenanceDroid
- `Player` → Interacts with `Location`, holds tool/crystal
- `GameController` → Creates and connects all objects, runs the game loop

---

