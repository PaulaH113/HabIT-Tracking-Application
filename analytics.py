
# This module uses the functional programming approach to analyse habit data; each function takes a habit or list of habits and returns useful information.

from datetime import datetime, timedelta 

''' The following function returns the allowed time gap for a given periodicity.

    daily → each completion must be within 1 day of the previous one
    weekly → each completion must be within 7 days of the previous one
    monthly → each completion must be within 30 days of the previous one
    yearly → each completion must be within 365 days of the previous one

'''

def get_periodicity_delta(periodicity):
    if periodicity == "daily":
        return timedelta(days=1)
    elif periodicity == "weekly":
        return timedelta(days=7)
    elif periodicity == "monthly":
        return timedelta(days=30)
    elif periodicity == "yearly":
        return timedelta(days=365)
    else:
        return timedelta(days=1)  # default to daily if unknown


''' Function that calculates the current streak for a habit. 
    Compares dates only, so multiple completions on the same day count as one.
'''

def get_streak(habit):
    if not habit.completions:
        return 0

    delta = get_periodicity_delta(habit.periodicity)
    sorted_dates = sorted(set(c.date() for c in habit.completions))

    if len(sorted_dates) == 1:
        return 1

    streak = 1
    for i in range(1, len(sorted_dates)):
        diff = sorted_dates[i] - sorted_dates[i - 1]
        if diff <= delta:
            streak += 1
        else:
            streak = 1

    return streak

# Function that calculates the longest streak ever recorded for a single habit.

def get_longest_streak(habit):
    
    if not habit.completions:
        return 0

    delta = get_periodicity_delta(habit.periodicity)
    sorted_dates = sorted(set(c.date() for c in habit.completions))

    longest = 1
    current = 1
    for i in range(1, len(sorted_dates)):
        diff = sorted_dates[i] - sorted_dates[i - 1]
        if diff <= delta:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1

    return longest


# Returns the longest streak value across all habits.

def get_longest_streak_all(habits):
    if not habits:
        return 0
    return max(get_longest_streak(habit) for habit in habits)


# Returns a list of all habit names.
def get_all_habits(habits):
    
    return [habit.name for habit in habits]


# Returns only the habits that match the given periodicity.

def get_habits_by_periodicity(habits, periodicity):
    return [habit for habit in habits if habit.periodicity == periodicity]


# Returns the habit with the highest current streak.

def get_most_consistent_habit(habits):
    
    if not habits:
        return None
    return max(habits, key=lambda h: get_streak(h))


# Returns the habit with the lowest current streak.

def get_struggling_habit(habits):
    if not habits:
        return None
    return min(habits, key=lambda h: get_streak(h))


# Return habits sorted by how many periods they missed in the last 30 days.
def get_struggling_habits_last_month(habits):
    today = datetime.now().date()
    thirty_days_ago = today - timedelta(days=30)

    results = []
    for habit in habits:
        recent = set(c.date() for c in habit.completions if c.date() >= thirty_days_ago)

        if habit.periodicity == "daily":
            expected = 30
        elif habit.periodicity == "weekly":
            expected = 4
        elif habit.periodicity == "monthly":
            expected = 1
        else:
            expected = 0

        missed = max(0, expected - len(recent))
        results.append((habit, missed))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
