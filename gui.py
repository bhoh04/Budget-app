import tkinter as tk
from tkinter import messagebox

class BudgetApp:
    def __init__(self, master):
        self.master = master
        master.title("Budget Tracker")

        self.label = tk.Label(master, text="Enter a transaction:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_transaction)
        self.submit_button.pack()

    def submit_transaction(self):
        transaction = self.entry.get()
        # Here you would process the transaction, for example:
        # Add it to the appropriate budget category
        # Update the display to show the current balance
        messagebox.showinfo("Transaction Submitted", f"Transaction '{transaction}' submitted successfully!")


root = tk.Tk()
app = BudgetApp(root)
root.mainloop()
