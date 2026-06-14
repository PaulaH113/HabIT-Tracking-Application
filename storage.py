# This module handles all database operations: creating tables, saving and loading habits and completions, using SQLite database (storage.db)

import sqlite3
from datetime import datetime
from tracker import Habit, HabitsTracker

# Create and return a connection to the database

def get_connection():
    return sqlite3.connect("storage.db")

#Create the tables if they don't exist yet

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            periodicity TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_name TEXT NOT NULL,
            completed_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

 # Save a new habit to the database

def save_habit(habit):
   
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO habits (name, periodicity, created_at)
        VALUES (?, ?, ?)
    """, (habit.name, habit.periodicity, str(habit.created_at)))

    conn.commit()
    conn.close()

# Save a completion entry for a habit

def save_completion(habit_name):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO completions (habit_name, completed_at)
        VALUES (?, ?)
    """, (habit_name, str(datetime.now())))

    conn.commit()
    conn.close()

# Load all habits and their completions from the database

def load_habits():
    
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("SELECT name, periodicity, created_at FROM habits")
    rows = cursor.fetchall()

    # fetchall() returns a list of rows, each row is a tuple: row[0] is the first column, row[1] the second, and so on

    habits = []
    for row in rows:
        habit = Habit(row[0], row[1])
        habit.created_at = datetime.fromisoformat(row[2])

        # load completions for this habit
        cursor.execute("""
            SELECT completed_at FROM completions
            WHERE habit_name = ?
        """, (row[0],))

        completions = cursor.fetchall()
        habit.completions = [datetime.fromisoformat(c[0]) for c in completions]
        habits.append(habit)

        # datetime.fromisoformat() converts the text we stored back into a proper datetime object

    conn.close()
    return habits

# Add predefined habits set if the database is empty

def add_predefined_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM habits")
    count = cursor.fetchone()[0]
    conn.close()

    if count == 0:  # only add if no habits exist yet
        predefined = [
            Habit("20 min exercise", "daily"),
            Habit("Drink 2L of water", "daily"),
            Habit("Read 30 minutes", "daily"),
            Habit("Run in the park", "weekly"),
            Habit("Meal prep", "weekly"),
            Habit("Cleaning and decluttering", "monthly"),
        ]
        for habit in predefined:
            save_habit(habit)
        print("Predefined habits loaded!")

''' Generate 4 weeks of test completions for predefined habits.
    It only runs once, if completions already exist, this function does nothing.
'''
def add_test_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM completions")
    count = cursor.fetchone()[0]
    conn.close()

    if count == 0:
        from datetime import timedelta
        today = datetime.now()

        # 20 min exercise; misses day 5 and day 12 

        missed_days = [5, 12]
        for day in range(28):
            if day not in missed_days:
                completion_date = today - timedelta(days=day)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                    ("20 min exercise", str(completion_date)))
                conn.commit()
                conn.close()

        # Drink 2L of water, day 20 missed 

        missed_days = [20]
        for day in range(28):
            if day not in missed_days:
                completion_date = today - timedelta(days=day)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                    ("Drink 2L of water", str(completion_date)))
                conn.commit()
                conn.close()

        # Read 30 minutes, missesed days: 2, 8, 9, 15, 21, 22

        missed_days = [2, 8, 9, 15, 21, 22]
        for day in range(28):
            if day not in missed_days:
                completion_date = today - timedelta(days=day)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                    ("Read 30 minutes", str(completion_date)))
                conn.commit()
                conn.close()

        # Run in the park, missed days: 14-20

        missed_weeks = [2]
        for week in range(4):
            if week not in missed_weeks:
                completion_date = today - timedelta(weeks=week)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                    ("Run in the park", str(completion_date)))
                conn.commit()
                conn.close()

        # Meal prep: fully consistent, all 4 weeks

        for week in range(4):
            completion_date = today - timedelta(weeks=week)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                ("Meal prep", str(completion_date)))
            conn.commit()
            conn.close()

        # Cleaning and decluttering: month 3 missed

        missed_months = [2]
        for month in range(4):
            if month not in missed_months:
                completion_date = today - timedelta(days=month * 30)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO completions (habit_name, completed_at) VALUES (?, ?)",
                    ("Cleaning and decluttering", str(completion_date)))
                conn.commit()
                conn.close()

        print("Test data loaded!")
