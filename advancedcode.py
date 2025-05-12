import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Database setup
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
)
''')
conn.commit()

# Functions for CRUD operations
def add_expense(date, category, amount, description):
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()

def update_expense(expense_id, date, category, amount, description):
    cursor.execute('''
        UPDATE expenses
        SET date = ?, category = ?, amount = ?, description = ?
        WHERE id = ?
    ''', (date, category, amount, description, expense_id))
    conn.commit()

def delete_expense(expense_id):
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()

def get_all_expenses():
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

def get_expenses_by_date_range(start_date, end_date):
    cursor.execute('''
        SELECT * FROM expenses WHERE date BETWEEN ? AND ?
    ''', (start_date, end_date))
    return cursor.fetchall()

# Visualization functions
def plot_expenses_by_category():
    df = pd.read_sql_query('SELECT category, SUM(amount) as total FROM expenses GROUP BY category', conn)
    plt.figure(figsize=(8,8))
    plt.pie(df['total'], labels=df['category'], autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.show()

def plot_expenses_over_time():
    df = pd.read_sql_query('SELECT date, SUM(amount) as total FROM expenses GROUP BY date', conn)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    plt.figure(figsize=(10,5))
    plt.plot(df['date'], df['total'], marker='o')
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Spent')
    plt.grid(True)
    plt.show()

# User Interface
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Show Expenses by Category")
        print("6. Show Expenses Over Time")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            date_str = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format.")
                continue
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_expense(date_str, category, amount, description)
            print("Expense added.")

        elif choice == '2':
            expenses = get_all_expenses()
            for exp in expenses:
                print(f"ID: {exp[0]}, Date: {exp[1]}, Category: {exp[2]}, Amount: {exp[3]}, Description: {exp[4]}")

        elif choice == '3':
            expense_id = int(input("Enter expense ID to update: "))
            date_str = input("Enter new date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format.")
                continue
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            description = input("Enter new description (optional): ")
            update_expense(expense_id, date_str, category, amount, description)
            print("Expense updated.")

        elif choice == '4':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted.")

        elif choice == '5':
            plot_expenses_by_category()

        elif choice == '6':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            expenses = get_expenses_by_date_range(start_date, end_date)
            df = pd.DataFrame(expenses, columns=['ID', 'Date', 'Category', 'Amount', 'Description'])
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date')
            plt.figure(figsize=(10,5))
            plt.plot(df['Date'], df['Amount'], marker='o')
            plt.title('Expenses Over Time')
            plt.xlabel('Date')
            plt.ylabel('Amount')
            plt.grid(True)
            plt.show()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == '__main__':
    main()
