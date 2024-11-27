
# Expense Tracker

This is a simple Expense Tracker application built using Python's Tkinter for the graphical user interface and pandas for data handling. The application allows users to add their expenses, categorize them, and view a summary of total expenses and a breakdown by category.

## Features

- Add expenses with the date, category, and amount.
- The date is entered in the format DD MM YYYY.
- Categorize expenses and track them separately.
- View a summary of total expenses and expenses by category.
- The data is stored in a CSV file (expenses.csv) for persistence.

## Requirements

To run this application, you need to have the following Python libraries installed:

- `pandas`
- `tkinter` (Usually pre-installed with Python)
- `datetime` (Usually pre-installed with Python)

You can install pandas using pip:

```bash
pip install pandas
```

## How to Use

1. Enter the expense details:
    - Date (DD MM YYYY)
    - Category (e.g., Food, Travel, etc.)
    - Amount (numerical value)

2. Click the "Add Expense" button to save the expense.
3. The summary of total expenses and expenses by category will be updated automatically.
4. The data is saved in a file named `expenses.csv`.

## File Structure

- `expenses.csv`: This file stores all the expense records in CSV format.
- `Expense Tracker.py`: The main Python script with the Tkinter application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

