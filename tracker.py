# This module defines the two core classes: Habit and HabitsTracker. It uses the object-oriented programming paradigm

from datetime import datetime

# Represents a single habit with its name, periodicity and completion history.

class Habit:
    def __init__(self, name, periodicity):
        self.name = name                  # e.g. "Exercise"
        self.periodicity = periodicity    # "daily", "weekly", "monthly", "yearly"
        self.created_at = datetime.now()  # auto-recorded when habit is created
        self.completions = []             # list of datetime objects, one per check-in

    # Mark this habit as done.

    def complete(self):
        
        self.completions.append(datetime.now())

    # Controls what gets printed after print(habit).

    def __str__(self):
        return f"{self.name} ({self.periodicity}) — {len(self.completions)} completions"



# Manages the collection of all tracked habits.

class HabitsTracker:
    def __init__(self):
        self.habits = []

    # Add a new habit, but only if it is not already being tracked.

    def add_habit(self, habit):
        for h in self.habits:
            if h.name.lower() == habit.name.lower():
                print(f"'{habit.name}' is already being tracked.")
                return
        self.habits.append(habit)
        print(f"'{habit.name}' added successfully!")

    # Remove a habit by name.

    def delete_habit(self, name):
        for h in self.habits:
            if h.name.lower() == name.lower():
                self.habits.remove(h)
                print(f"'{name}' deleted.")
                return
        print(f"'{name}' not found.")

    # Find and return a single habit by name, or None if not found.

    def get_habit(self, name):
        for h in self.habits:
            if h.name.lower() == name.lower():
                return h
        return None
