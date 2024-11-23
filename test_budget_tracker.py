import unittest
from anitha_PLD2 import budgetboss
from eff_PLD2 import calculate_total, SavingsGoal

class TestBudgetBoss(unittest.TestCase):
    def test_set_budget(self):
        bb = budgetboss()
        bb.budget = 100.0  # Mock user input
        self.assertEqual(bb.budget, 100.0)

    def test_update_budget(self):
        bb = budgetboss()
        bb.budget = 50.0
        bb.budget = 75.0  # Mock user update
        self.assertEqual(bb.budget, 75.0)

class TestExpenseTracking(unittest.TestCase):
    def test_calculate_total(self):
        sample_expenses = {"1": {"cost": "10", "item": "pen"}, "2": {"cost": "20", "item": "book"}}
        total = calculate_total(sample_expenses)
        self.assertEqual(total, 30.0)

    def test_savings_goal_progress(self):
        goal = SavingsGoal("New Car", 5000)
        goal.add_savings(1000)
        self.assertEqual(goal.current_savings, 1000)
        self.assertEqual(goal.progress_percentage(), 20.0)

if __name__ == "__main__":
    unittest.main()
