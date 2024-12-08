import csv

def add_expense(expenses):

    try:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense (e.g: Food, Travel, Accommodation): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ")

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please ensure the amount is a number and try again.")

def view_expenses(expenses):

    if not expenses:
        print("No expenses to display.")
        return

    print("\nStored Expenses:")
    for i, expense in enumerate(expenses, start=1):
        if not all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']):
            print(f"Expense {i} is incomplete and will be skipped.")
            continue

        print(f"Expense {i}:")
        print(f"  Date: {expense['date']}")
        print(f"  Category: {expense['category']}")
        print(f"  Amount: {expense['amount']}")
        print(f"  Description: {expense['description']}")
        print("-" * 30)

def set_budget():
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {budget:.2f}")
        return budget
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0.0

def calculate_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses if 'amount' in expense)

def check_budget(budget, expenses):
    total_expenses = calculate_total_expenses(expenses)
    print(f"\nTotal Expenses: {total_expenses:.2f}")
    if total_expenses > budget:
        print("budget",budget)
        print("Warning: You have exceeded your budget!")
    else:
        remaining = budget - total_expenses
        print(f"You have {remaining:.2f} left for the month.")

def save_expenses_to_csv(expenses, filename="expenses.csv"):

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expenses saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

def load_expenses_from_csv(filename="expenses.csv"):

    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert amount back to float
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing file found at {filename}. Starting with an empty list.")
    except Exception as e:
        print(f"An error occurred while loading from CSV: {e}")
    return expenses

# Example usage
if __name__ == "__main__":
    expenses = load_expenses_from_csv()  # Load expenses on startup
    budget = 0.0

    while True:
        print("\nMenu:")
        print("1. Set Monthly Budget")
        print("2. Add an Expense")
        print("3. View Expenses")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            budget = set_budget()
        elif choice == '2':
            add_expense(expenses)
        elif choice == '3':
            view_expenses(expenses)
        elif choice == '4':
            check_budget(budget, expenses)
        elif choice == '5':
            save_expenses_to_csv(expenses)
        elif choice == '6':
            save_expenses_to_csv(expenses)  # Save on exit
            print("Exiting the program !")
            break
        else:
            print("Please choose from 1 to 6 option. Please try again.")