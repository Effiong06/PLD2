import json

def expense_input():
    # Get input for cost and purchased item
    x = input("Write cost: ")  # Cost
    y = input("What did you purchase?: ")  # Item purchased
    return x, y  # Return both inputs

def save_data(expenses_input):
    # Save the dictionary to a JSON file
    with open("expenses.json", "w") as f:
        json.dump(expenses_input, f)
    print("Data saved successfully!")

def load_data():
    # Load data from a JSON file, if it exists
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # If the file doesn't exist, return an empty dictionary

def display_costs(expenses_input):
    # Display just the costs from the dictionary
    print("\nList of All Costs:")
    for entry in expenses_input.values():
        print(entry['cost'])

def calculate_total(expenses_input):
    # Calculate the total sum of all the costs
    total = 0
    for entry in expenses_input.values():
        cost = entry['cost'].replace('$', '').strip()
        total += float(cost)
    return total

def main():
    # Step 1: Get the user's initial budget
    budget = float(input("Enter your initial budget for today: $"))

    # Step 2: Load any existing data from the JSON file
    expenses_input = load_data()

    # Find the next available entry number
    counter = len(expenses_input) + 1
    
    # Step 3: Run a loop to allow multiple users to input their expenses
    while True:
        # Step 4: Get expense data
        x, y = expense_input()
        
        # Step 5: Store the expense data in the dictionary with a unique key
        expenses_input[counter] = {"cost": x, "item": y}
        
        # Print the current entry
        print(f"Entry {counter}: Cost = {x}, Item = {y}")
        
        # Increment the counter for the next entry
        counter += 1
        
        # Ask if the user wants to add another expense
        another = input("Do you want to enter another expense? (yes/no): ").strip().lower()
        if another == 'no':
            break  # Exit the loop if the user doesn't want to continue

    # Step 6: Print all entered expenses as a dictionary
    print("\nAll entered expenses:")
    print(expenses_input)
    
    # Step 7: Save the updated dictionary to the JSON file
    save_data(expenses_input)

    # Step 8: Display costs after all expenses are entered and saved
    display_costs(expenses_input)

    # Step 9: Calculate the total expenses
    total_expenses = calculate_total(expenses_input)
    print(f"\nYour total expenses for today are: ${total_expenses:.2f}")

    # Step 10: Compare the total expenses to the budget
    if total_expenses > budget:
        print(f"\nYou have exceeded your budget by: ${total_expenses - budget:.2f}")
    else:
        print(f"\nYou are within your budget! You have ${budget - total_expenses:.2f} remaining.")

# Run the main function
main()
