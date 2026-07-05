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
<img width="568" height="302" alt="Screenshot 2026-07-05 at 14 04 20" src="https://github.com/user-attachments/assets/77bb621c-f784-4873-91e3-854e60201c28" />

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

<img width="493" height="218" alt="Screenshot 2026-07-05 at 14 07 09" src="https://github.com/user-attachments/assets/1c49b856-0f55-4b97-8208-0e03ccb1d195" />


### Completing a Habit

1. Select option **3** from the main menu
2. A list of all currently tracked habits will be displayed
3. Enter the name of the habit you completed
4. If the habit is not found, the application will ask if you wish to add it as a new habit

**Perfect Day:** Type `perfect day` when prompted to mark all daily habits as complete in one go.

<img width="516" height="337" alt="Screenshot 2026-07-05 at 14 09 43" src="https://github.com/user-attachments/assets/d0bd74be-e940-4012-9bba-de2cefddea55" />

<img width="533" height="148" alt="Screenshot 2026-07-05 at 14 14 46" src="https://github.com/user-attachments/assets/7bda0b75-fe64-4dd0-bf23-c92053ffa3b0" />


### Viewing Streaks

Select option **5** to view the current and longest streak for each tracked habit.

A streak increases by one for each consecutive period (day, week, month or year) in which the habit is completed. If a period is missed, the streak resets to zero.

<img width="528" height="244" alt="Screenshot 2026-07-05 at 14 10 28" src="https://github.com/user-attachments/assets/bc5d4a47-9753-4e57-a01e-c6f275a13ba4" />


### Viewing Analytics

Select option **6** to view:
- Longest streak across all habits
- Most consistent habit
- Habit needing most attention
- Habits grouped by periodicity

<img width="557" height="411" alt="Screenshot 2026-07-05 at 14 11 20" src="https://github.com/user-attachments/assets/7cf6d3e5-4f3a-4cc6-98f8-7d2afddcaec1" />


### Exit the Application

Select option **7** to exit.

<img width="480" height="166" alt="Screenshot 2026-07-05 at 14 11 57" src="https://github.com/user-attachments/assets/d5221ecc-c5a4-4423-ae30-65ffb2db5ba7" />


