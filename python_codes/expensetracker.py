import pandas as pd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# File where expenses will be saved
FILE_PATH = "expenses.csv"

# Initialize or load the DataFrame
try:
    df = pd.read_csv(FILE_PATH)
except FileNotFoundError:
    # Create an empty DataFrame if file does not exist
    df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Function to add expense
def add_expense():
    day = entry_day.get()
    month = entry_month.get()
    year = entry_year.get()
    category = entry_category.get()

    # Validate amount input
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return

    # Combine date fields into YYYY-MM-DD format
    try:
        date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date.")
        return

    # Append data to the DataFrame using pandas.concat
    global df
    new_row = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated DataFrame to CSV
    df.to_csv(FILE_PATH, index=False)

    # Clear the input fields
    entry_day.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    # Update summary display
    update_summary()
    messagebox.showinfo("Expense Added", "Your expense has been added successfully!")

# Function to update summary display
def update_summary():
    if not df.empty:
        total_expense = df['Amount'].sum()
        category_summary = df.groupby('Category')['Amount'].sum()

        summary_text = f"Total Expenses: \u20B9{total_expense:.2f}\n\n"
        summary_text += "Expenses by Category:\n"
        for category, amount in category_summary.items():
            summary_text += f"{category}: \u20B9{amount:.2f}\n"
    else:
        summary_text = "No expenses to show."

    label_summary.config(text=summary_text)

# Initialize Tkinter window
root = tk.Tk()
root.title("Expense Tracker")

# Create input fields and labels
tk.Label(root, text="Date (DD MM YYYY):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_day = tk.Entry(root, width=4)
entry_day.grid(row=0, column=1, padx=2, pady=5, sticky="w")
entry_month = tk.Entry(root, width=4)
entry_month.grid(row=0, column=1, padx=40, pady=5, sticky="w")
entry_year = tk.Entry(root, width=6)
entry_year.grid(row=0, column=1, padx=80, pady=5, sticky="w")

tk.Label(root, text="Category:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_category = tk.Entry(root, width=20)
entry_category.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_amount = tk.Entry(root, width=20)
entry_amount.grid(row=2, column=1, padx=10, pady=5)

# Add button to submit expense
btn_add = tk.Button(root, text="Add Expense", command=add_expense)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

# Label for displaying summary
label_summary = tk.Label(root, text="", justify="left", font=("Arial", 10))
label_summary.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Initialize summary display
update_summary()

# Run the Tkinter event loop
root.mainloop()
