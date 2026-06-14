# HabIT 
A Habit Tracking Application

## Overview

HabIT is a command-line habit tracking application developed in Python. It allows users to create, track and analyse personal habits. The application is built around two core concepts: **habits** (regular activities the user wishes to reinforce) and **streaks** (consecutive periods in which a habit has been completed).

The application follows a modular architecture, combining object-oriented programming for habit management with a functional approach for analytics, and SQLite for data persistence.

---

## Requirements

- Python 3.8 or higher
- HabIT uses only Python standard libraries, and no external libraries required.

---

## Installation

1. Clone or download the project folder to your computer.
2. Navigate to the project directory in your terminal:

```bash
cd path/to/HabIT
```

3. Verify Python is installed:

```bash
python3 --version
```

---

## Running the Application

To start the application, run the following command from the project directory:

```bash
python3 main.py
```

On first launch, the application will automatically:
- Create the SQLite database (`storage.db`)
- Load a set of predefined habits
- Generate 4 weeks of example tracking data

---

## Using the Application

Upon launch, the user is presented with the following menu:

1. Add a habit
2. Delete a habit
3. Mark a habit as complete
4. Show all habits
5. Show streaks
6. Show analytics
7. Exit

### Creating a New Habit

1. Select option **1** from the main menu
2. Enter the habit name (e.g. `Meditate`)
3. Enter the periodicity — must be one of: `daily`, `weekly`, `monthly`, `yearly`

The habit will be saved to the database.

### Completing a Habit

1. Select option **3** from the main menu
2. A list of all currently tracked habits will be displayed
3. Enter the name of the habit you completed
4. If the habit is not found, the application will ask if you wish to add it as a new habit

> **Perfect Day:** Type `perfect day` when prompted to mark all daily habits as complete in one go.

### Viewing Streaks

Select option **5** to view the current and longest streak for each tracked habit.

A streak increases by one for each consecutive period (day, week, month or year) in which the habit is completed. If a period is missed, the streak resets to zero.

### Viewing Analytics

Select option **6** to view:
- Longest streak across all habits
- Most consistent habit
- Habit needing most attention
- Habits grouped by periodicity

### Exit the Application

Select option **7** to exit.

---

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point — CLI menu and user interaction |
| `tracker.py` | `Habit` and `HabitsTracker` class definitions |
| `storage.py` | SQLite database operations — save, load, initialise |
| `analytics.py` | Functional analytics — streaks, consistency, analysis |
| `test.py` | Unit tests using Python's `unittest` framework |
| `storage.db` | Auto-generated SQLite database file |

---

## Predefined Habits

The following habits are loaded automatically on first launch:

| Habit | Periodicity |
|-------|-------------|
| 20 min exercise | Daily |
| Drink 2L of water | Daily |
| Read 30 minutes | Daily |
| Run in the park | Weekly |
| Meal prep | Weekly |
| Cleaning and decluttering | Monthly |
