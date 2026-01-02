import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        m1 = int(e1.get())
        m2 = int(e2.get())
        m3 = int(e3.get())

        # Marks must be between 0 and 100
        if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
            messagebox.showerror("Error", "Marks must be between 0 and 100")
            return

        total = m1 + m2 + m3
        average = total / 3

        if average >= 80:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        lbl_total.config(text=f"Total: {total}")
        lbl_avg.config(text=f"Average: {average:.2f}")
        lbl_grade.config(text=f"Grade: {grade}")

    except ValueError:
        messagebox.showerror("Error", "Enter numbers only")

# Window
root = tk.Tk()
root.title("Student Marks Calculator")
root.geometry("340x360")
root.config(bg="#f5f5f5")

# Heading with background color
tk.Label(
    root,
    text="Student Marks Calculator",
    font=("Arial", 16, "bold"),
    bg="#4CAF50",      # Green background
    fg="white",
    relief="solid",
    bd=2,
    padx=10,
    pady=8
).pack(pady=12, fill="x")

# Inputs
tk.Label(root, text="Subject 1 (0-100)", bg="#f5f5f5").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Subject 2 (0-100)", bg="#f5f5f5").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Label(root, text="Subject 3 (0-100)", bg="#f5f5f5").pack()
e3 = tk.Entry(root)
e3.pack()

# Button
tk.Button(
    root,
    text="Calculate",
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    command=calculate
).pack(pady=12)

# Results
lbl_total = tk.Label(root, text="Total:", bg="#f5f5f5")
lbl_total.pack()

lbl_avg = tk.Label(root, text="Average:", bg="#f5f5f5")
lbl_avg.pack()

lbl_grade = tk.Label(root, text="Grade:", bg="#f5f5f5")
lbl_grade.pack()

root.mainloop()
