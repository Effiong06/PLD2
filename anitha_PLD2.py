#!/usr/bin/env python3

import sys

class budgetboss:
    def __init__(self):
        self.budget = 0.0

    def set_budget(self):
        """set a new budget with input validation."""
        while True:
            try:
                user_input = input("enter your budget amount: $")
                budget_amount = float(user_input)
                if budget_amount < 0:
                    print("budget amount must be a positive number")
                else:
                    self.budget = budget_amount
                    print(f"budget set to: ${self.budget:.2f}")
                    break
            except ValueError:
                print("Invalid input! please enter a valid number.")

    def update_budget(self):
        """allow user to update the budget."""
        while True:
            try:
                user_input = input("Enter the new budget amount: $")
                budget_amount = float(user_input)
                if budget_amount < 0:
                    print("Budget amount must be a positive number")
                else:
                    self.budget = budget_amount
                    print(f"budget updated to: ${self.budget:.2f}")
                    break
            except ValueError:
                print("invalid input! please enter a valid number.")

    def view_budget(self):
        """display the current budget."""
        if self.budget == 0.0:
            print("no budget has been set yet")
        else:
            print(f"your current budget is : ${self.budget:.2f}")

def main():
    budget_boss = budgetboss()

    while True:
        print("\nBudget Boss Menu")
        print("1. Set Budget")
        print("2. Update Budget")
        print("3. View Budget")
        print("4. Exit")

        choice = input("choose an option: ")

        if choice == '1':
            budget_boss.set_budget()
        elif choice == '2':
            budget_boss.update_budget()
        elif choice == '3':
            budget_boss.view_budget()
        elif choice == '4':
            print("exiting budget boss. Goodbye!")
            sys.exit()
        else:
            print("invalid option! choose a valid option.")

if __name__ == "__main__":
    main()




