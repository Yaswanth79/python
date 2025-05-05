import sqlite3

def create_table():
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            description TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(description, amount):
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (description, amount) VALUES (?, ?)', (description, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    rows = c.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect('budget.db')
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(description, amount)
            print("Expense added.")
        elif choice == '2':
            expenses = view_expenses()
            for expense in expenses:
                print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}")
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
