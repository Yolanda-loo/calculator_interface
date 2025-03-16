import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    """Handles button clicks and performs operations."""
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main application window
app = tk.Tk()
app.title("My calculator")
app.geometry("300x400")

# Entry widget for the display
entry = tk.Entry(app, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons dynamically
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(
        app,
        text=button_text,
        font=("Arial", 15),
        bg="grey",   # Setting button color to grey
        fg="white",
        width=5,
        height=2,
        command=lambda bt=button_text: on_click(bt)
    )
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
