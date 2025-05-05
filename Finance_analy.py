import csv
from datetime import datetime

def add_transaction(filename, description, amount):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), description, amount])

def view_transactions(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    filename = 'expenses.csv'
    while True:
        action = input("Choose action: [add/view/exit]: ").strip().lower()
        if action == 'add':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_transaction(filename, description, amount)
        elif action == 'view':
            view_transactions(filename)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please choose 'add', 'view', or 'exit'.")
