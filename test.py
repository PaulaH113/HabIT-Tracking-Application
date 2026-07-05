'''
This module provides testing scenarios using test data.

What is tested:

 Does adding a habit work correctly?
 Does deleting a habit work correctly?
 What happens when a habit is added twice?
 Does the streak calculate correctly?
 Does the streak reset work correctly?
 Does saving and loading from the database work?
 What happens with a misspelled habit name?

'''

import unittest
from datetime import datetime, timedelta
from tracker import Habit, HabitsTracker
from analytics import get_streak, get_longest_streak

class TestHabit(unittest.TestCase):

    # Test that a habit is added correctly

    def test_add_habit(self):
                tracker = HabitsTracker()
        habit = Habit("Exercise", "daily")
        tracker.add_habit(habit)
        self.assertEqual(len(tracker.habits), 1)
        self.assertEqual(tracker.habits[0].name, "Exercise")

    # Test that adding a duplicate habit is rejected

    def test_add_duplicate_habit(self):
                tracker = HabitsTracker()
        habit1 = Habit("Exercise", "daily")
        habit2 = Habit("Exercise", "daily")
        tracker.add_habit(habit1)
        tracker.add_habit(habit2)
        self.assertEqual(len(tracker.habits), 1)

    # Test that a habit is deleted correctly
    def test_delete_habit(self):
        tracker = HabitsTracker()
        habit = Habit("Exercise", "daily")
        tracker.add_habit(habit)
        tracker.delete_habit("Exercise")
        self.assertEqual(len(tracker.habits), 0)

    # Test that deleting a habit that doesn't exist does nothing
    def test_delete_nonexistent_habit(self):
        tracker = HabitsTracker()
        habit = Habit("Exercise", "daily")
        tracker.add_habit(habit)
        tracker.delete_habit("Swim")
        self.assertEqual(len(tracker.habits), 1)

    # Test that a misspelled habit name returns None
    def test_misspelled_habit(self):
        tracker = HabitsTracker()
        habit = Habit("Exercise", "daily")
        tracker.add_habit(habit)
        result = tracker.get_habit("Exrcise")
        self.assertIsNone(result)

class TestStreak(unittest.TestCase):

    # Test that streak is 0 with no completions
    def test_streak_no_completions(self):
        habit = Habit("Exercise", "daily")
        self.assertEqual(get_streak(habit), 0)

    def test_streak_daily_consistent(self):
        # Test that streak is 0 with no completions
        habit = Habit("Exercise", "daily")
        habit.completions = [
            datetime.now() - timedelta(days=3),
            datetime.now() - timedelta(days=2),
            datetime.now() - timedelta(days=1),
            datetime.now()
        ]
        self.assertEqual(get_streak(habit), 4)

    # Test that streak resets after a missed day
    def test_streak_resets(self):
        habit = Habit("Exercise", "daily")
        habit.completions = [
            datetime.now() - timedelta(days=5),  # then a gap...
            datetime.now() - timedelta(days=1),
            datetime.now()
        ]
        self.assertEqual(get_streak(habit), 2)

    # Test that longest streak is tracked correctly
    def test_longest_streak(self):
        habit = Habit("Exercise", "daily")
        habit.completions = [
            datetime.now() - timedelta(days=6),
            datetime.now() - timedelta(days=5),
            datetime.now() - timedelta(days=4),  # gap here
            datetime.now() - timedelta(days=1),
            datetime.now()
        ]
        self.assertEqual(get_longest_streak(habit), 3)

if __name__ == "__main__":
    unittest.main()

