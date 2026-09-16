import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI")
window.geometry("400x300")

# Text
title = tk.Label(window, text="Solitaire GUI Practice", font=("Arial", 18))
title.pack(pady=10)

# Canvas for lines and text
canvas = tk.Canvas(window, width=350, height=80)
canvas.pack()

# Lines
canvas.create_line(50, 20, 300, 20, width=2)
canvas.create_line(50, 60, 300, 60, width=2)

# Text on the canvas
canvas.create_text(175, 40, text="Card Area")

# Check box
sound_var = tk.BooleanVar()
sound_checkbox = tk.Checkbutton(
    window,
    text="Enable Sound",
    variable=sound_var
)
sound_checkbox.pack(pady=5)

# Radio buttons
difficulty = tk.StringVar(value="Easy")

easy_radio = tk.Radiobutton(
    window,
    text="Easy",
    variable=difficulty,
    value="Easy"
)
easy_radio.pack()

hard_radio = tk.Radiobutton(
    window,
    text="Hard",
    variable=difficulty,
    value="Hard"
)
hard_radio.pack()

# Start the GUI
window.mainloop()