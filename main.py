from tracker import Habit, HabitsTracker
from storage import initialize_db, save_habit, save_completion, load_habits, add_predefined_habits, add_test_data
from analytics import get_streak, get_longest_streak, get_longest_streak_all, get_all_habits, get_habits_by_periodicity, get_most_consistent_habit, get_struggling_habit, get_struggling_habits_last_month

# Function that asks for periodicity until a valid one is entered, to avoid spelling mistakes
def get_valid_periodicity():
    valid = ["daily", "weekly", "monthly", "yearly"]
    while True:
        print("Periodicity: daily / weekly / monthly / yearly")
        periodicity = input("Choose periodicity: ").lower().strip()
        if periodicity in valid:
            return periodicity
        print("Invalid periodicity! Please choose from: daily, weekly, monthly, yearly")


# Main function, coroborating the entire project logic
def main():
    initialize_db()
    add_predefined_habits()
    add_test_data()
    tracker = HabitsTracker()

    # loading existing habits from database
    for habit in load_habits():
        tracker.habits.append(habit)

    while True:
        print("\n--- HabIT ---")
        print("1. Add a habit")
        print("2. Delete a habit")
        print("3. Mark a habit as complete")
        print("4. Show all habits")
        print("5. Show streaks")
        print("6. Show analytics")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = get_valid_periodicity()
            habit = Habit(name, periodicity)
            tracker.add_habit(habit)
            save_habit(habit)

        elif choice == "2":
            print("\nYour habits:")
            for h in tracker.habits:
                print(f"  - {h.name}")
            name = input("\nHabit name to delete: ")
            tracker.delete_habit(name)

        elif choice == "3":
            # show available habits first
            print("\nYour habits:")
            for h in tracker.habits:
                print(f"  - {h.name} ({h.periodicity})")

            print("\nTip: type 'perfect day' to complete all daily habits at once!")
            name = input("\nWhich habit did you complete? ")

            if name.lower().strip() == "perfect day":
                daily_habits = get_habits_by_periodicity(tracker.habits, "daily")
                if daily_habits:
                    for habit in daily_habits:
                        habit.complete()
                        save_completion(habit.name)
                    print("\n Perfect Daily Streak! All daily habits completed!")
                    print("Habits completed:")
                    for habit in daily_habits:
                        print(f"  {habit.name}")
                else:
                    print("No daily habits found!")

            else:
                habit = tracker.get_habit(name)

                if habit:
                    habit.complete()
                    save_completion(name)
                    print(f"'{name}' marked as complete!")
                else:
                    print(f"'{name}' not found in your habits.")
                    add_new = input(f"Would you like to add '{name}' as a new habit? (yes/no): ")
                    if add_new.lower() == "yes":
                        periodicity = get_valid_periodicity()
                        new_habit = Habit(name, periodicity)
                        tracker.add_habit(new_habit)
                        save_habit(new_habit)
                        new_habit.complete()
                        save_completion(name)
                        print(f"'{name}' added and marked as complete!")
                    else:
                        print("Ok, going back to the menu — check for typos!")

        elif choice == "4":
            if tracker.habits:
                for habit in tracker.habits:
                    print(f"  - {habit.name} ({habit.periodicity}) — created: {habit.created_at.strftime('%Y-%m-%d %H:%M')}")
            else:
                print("No habits yet!")

        elif choice == "5":
            if tracker.habits:
                for habit in tracker.habits:
                    print(f"  {habit.name}: current streak = {get_streak(habit)}, longest = {get_longest_streak(habit)}")
            else:
                print("No habits yet!")

        elif choice == "6":
            if tracker.habits:
                most = get_most_consistent_habit(tracker.habits)
                struggling = get_struggling_habit(tracker.habits)
                longest = get_longest_streak_all(tracker.habits)
                print(f"\nLongest streak across all habits: {longest}")
                print(f"Most consistent habit: {most.name}")
                print(f"Habit needing attention: {struggling.name}")
                print("\nHabits by periodicity:")
                for p in ["daily", "weekly", "monthly", "yearly"]:
                    filtered = get_habits_by_periodicity(tracker.habits, p)
                    if filtered:
                        print(f"  {p}: {[h.name for h in filtered]}")
                print("\n--- Struggling Habits Last Month ---")
                results = get_struggling_habits_last_month(tracker.habits)
                for habit, missed in results:
                    if missed == 0:
                        print(f"  {habit.name} — no missed periods!")
                    else:
                        print(f"   {habit.name} — missed {missed} period(s)")
            else:
                print("No habits yet!")


        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

'''
Clarifications:

while True creates an infinite loop — the menu keeps showing until the user chooses 7
break exits the loop
input() waits for the user to type something and press Enter
We load habits from the database at the start so data persists between sessions
'''