# HabIT 

HabIT is a command-line habit tracking application developed in Python. It allows users to create, track and analyse personal habits. 


## Requirements

- Python 3.8 or higher
- HabIT uses only Python standard libraries, no external libraries required


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

## Running the Application

To start the application, run the following command from the project directory:

```bash
python3 main.py
```

On the first launch, the application will automatically create the database, load predefined habits and generate 4 weeks of test data.

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
3. Enter the periodicity (must be one of: `daily`, `weekly`, `monthly`, `yearly`)

The habit will be saved to the database.

### Completing a Habit

1. Select option **3** from the main menu
2. A list of all currently tracked habits will be displayed
3. Enter the name of the habit you completed
4. If the habit is not found, the application will ask if you wish to add it as a new habit

**Perfect Day:** Type `perfect day` when prompted to mark all daily habits as complete in one go.

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


## Predefined Habits

The Application comes with the following habits, that are loaded automatically on first launch:

-> 20 min exercise (Daily)
-> Drink 2L of water (Daily)
-> Read 30 minutes (Daily)
-> Run in the park (Weekly)
-> Meal prep (Weekly)
-> Cleaning and decluttering (Monthly)
