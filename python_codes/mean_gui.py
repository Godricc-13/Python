import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from mean import load_csv, analyze_data, visualize_data
import matplotlib.pyplot as plt

# Open file dialog
def open_file():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:
        data = load_csv(file)
        if data is not None:
            show_analysis(data)

# Display analysis results
def show_analysis(data):
    win = tk.Toplevel()
    win.title("Data Analysis")
    win.geometry("600x500")

    # Perform analysis
    analysis = analyze_data(data)

    # Show analysis
    if analysis:
        text = tk.Text(win, wrap="word", height=15)
        text.pack(pady=10)
        for stat, values in analysis.items():
            text.insert("end", f"{stat}:\n{values}\n\n")

    # Visualization options
    tk.Label(win, text="Select columns to visualize:", font=("Arial", 10)).pack()
    cols = data.columns.tolist()
    selected_cols = {col: tk.BooleanVar() for col in cols}
    for col in cols:
        ttk.Checkbutton(win, text=col, variable=selected_cols[col]).pack(anchor="w")

    # Plot button
    def plot():
        selected = [col for col, var in selected_cols.items() if var.get()]
        if selected:
            visualize_data(data, selected)
        else:
            messagebox.showwarning("No Selection", "Please select at least one column.")

    ttk.Button(win, text="Plot", command=plot).pack(pady=10)

# Main GUI
def main_gui():
    root = tk.Tk()
    root.title("CSV Data Analysis")
    root.geometry("600x400")

    tk.Label(
        root,
        text="Load a CSV file to perform basic analysis (mean, median, mode) and visualize results.",
        font=("Arial", 12),
        justify="center",
        wraplength=500,
    ).pack(pady=20)

    ttk.Button(root, text="Open CSV", command=open_file).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
