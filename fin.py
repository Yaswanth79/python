import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
import numpy as np

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.balance = 1000.0
        self.transactions = []
        self.categories = []

        # Create labels and entries
        tk.Label(root, text="Balance: $").grid(row=0, column=0)
        self.balance_label = tk.Label(root, text=f"${self.balance:.2f}")
        self.balance_label.grid(row=0, column=1)

        tk.Label(root, text="Transaction Type (Income/Expense):").grid(row=1, column=0)
        self.transaction_type = tk.StringVar()
        self.transaction_type.set("Expense")
        self.transaction_type_menu = tk.OptionMenu(root, self.transaction_type, "Income", "Expense")
        self.transaction_type_menu.grid(row=1, column=1)

        tk.Label(root, text="Amount: $").grid(row=2, column=0)
        self.amount = tk.StringVar()
        self.amount_entry = tk.Entry(root, textvariable=self.amount)
        self.amount_entry.grid(row=2, column=1)

        tk.Label(root, text="Category:").grid(row=3, column=0)
        self.category = tk.StringVar()
        self.category_entry = tk.Entry(root, textvariable=self.category)
        self.category_entry.grid(row=3, column=1)

        # Create buttons
        tk.Button(root, text="Add Transaction", command=self.add_transaction).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="Delete Transaction", command=self.delete_transaction).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="View Transactions", command=self.view_transactions).grid(row=6, column=0, columnspan=2)
        tk.Button(root, text="Analyze Spending", command=self.analyze_spending).grid(row=7, column=0, columnspan=2)

    def add_transaction(self):
        try:
            amount = float(self.amount.get())
            category = self.category.get()
            if category not in self.categories:
                self.categories.append(category)

            if self.transaction_type.get() == "Income":
                self.balance += amount
            elif self.transaction_type.get() == "Expense":
                self.balance -= amount

            self.transactions.append((self.transaction_type.get(), amount, category))
            self.balance_label.config(text=f"${self.balance:.2f}")
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def delete_transaction(self):
        if not self.transactions:
            messagebox.showerror("Error", "No transactions to delete")
            return

        transaction_list = "\n".join([f"{i + 1}. {t[0]} - ${t[1]:.2f} ({t[2]})" for i, t in enumerate(self.transactions)])
        transaction_index = simpledialog.askinteger("Delete Transaction", f"Select transaction number to delete:\n{transaction_list}")

        if transaction_index is not None and 1 <= transaction_index <= len(self.transactions):
            transaction_type, amount, category = self.transactions[transaction_index - 1]
            if transaction_type == "Income":
                self.balance -= amount
            elif self.transaction_type.get() == "Expense":
                self.balance += amount
            del self.transactions[transaction_index - 1]
            self.balance_label.config(text=f"${self.balance:.2f}")
        else:
            messagebox.showerror("Error", "Invalid transaction number")

    def view_transactions(self):
        if self.transactions:
            transaction_list = "Transactions:\n"
            for i, (transaction_type, amount, category) in enumerate(self.transactions):
                transaction_list += f"{i + 1}. {transaction_type} - ${amount:.2f} ({category})\n"
            messagebox.showinfo("Transactions", transaction_list)
        else:
            messagebox.showerror("Error", "No transactions to view")

    def analyze_spending(self):
        if not self.transactions:
            messagebox.showerror("Error", "No transactions to analyze")
            return

        expense_data = []
        labels = []
        for category in self.categories:
            total_expense = sum(t[1] for t in self.transactions if t[0] == "Expense" and t[2] == category)
            expense_data.append(total_expense)
            labels.append(category)

        if expense_data:
            plt.figure(figsize=(8, 6))
            plt.pie(expense_data, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title("Spending Analysis")
            plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()