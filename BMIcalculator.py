import tkinter as tk
from tkinter import messagebox


# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())

        if weight <= 0 or feet < 0 or inches < 0:
            messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")
            return

        total_height = (feet * 12) + inches

        bmi = (weight / (total_height ** 2)) * 703

        if bmi < 18.5:
            category = "Underweight"
            note = "You may need to gain some weight."
        elif bmi < 25:
            category = "Normal"
            note = "You are in a healthy range."
        elif bmi < 30:
            category = "Overweight"
            note = "You may want to make lifestyle changes."
        else:
            category = "Obese"
            note = "Consider speaking with a healthcare professional."

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}\n{note}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")

# Clear inputs
def clear_fields():
    weight_entry.delete(0, tk.END)
    feet_entry.delete(0, tk.END)
    inches_entry.delete(0, tk.END)
    result_label.config(text="Your BMI result will appear here.")


title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

weight_label = tk.Label(root, text="Enter weight (lbs):", font=("Arial", 12))
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 12), justify="center")
weight_entry.pack(pady=5)

feet_label = tk.Label(root, text="Height (feet):", font=("Arial", 12))
feet_label.pack()
feet_entry = tk.Entry(root, font=("Arial", 12), justify="center")
feet_entry.pack(pady=5)

inches_label = tk.Label(root, text="Extra inches:", font=("Arial", 12))
inches_label.pack()
inches_entry = tk.Entry(root, font=("Arial", 12), justify="center")
inches_entry.pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12),
    command=calculate_bmi
)
calculate_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    command=clear_fields
)
clear_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Your BMI result will appear here.",
    font=("Arial", 12),
    wraplength=320,
    justify="center"
)
result_label.pack(pady=15)

root.mainloop()