
# Expense Tracker

This is a Python-based command-line application that allows users to manage and track their monthly expenses. The program provides functionalities to set a budget, add expenses, view expense history, monitor the budget, and save or load data from a CSV file for persistence.

---

## Features

### 1. Set Monthly Budget
- Allows the user to set a spending limit for the month.
- Helps in monitoring and planning finances.

### 2. Add Expense
- Users can record individual expenses with the following details:
  - **Date**: The date of the expense in `YYYY-MM-DD` format.
  - **Category**: Type of expense (e.g., Food, Travel, Accommodation).
  - **Amount**: The amount spent (numeric input).
  - **Description**: A brief note about the expense.

### 3. View Expenses
- Displays a list of all recorded expenses in a readable format.
- Skips incomplete or invalid entries.

### 4. Track Budget
- Calculates the total expenses and compares them with the set budget.
- Alerts the user if the total expenses exceed the budget or shows the remaining balance.

### 5. Save Expenses
- Saves the recorded expenses to a CSV file (`expenses.csv`) for persistence.

### 6. Load Expenses
- Loads existing expense records from the CSV file on startup, allowing users to continue from where they left off.

---

## Prerequisites

- **Python**: Ensure Python 3.x is installed on your system.

---

## How to Run

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd expense-tracker


Run the Program
> python expense_tracker.py
