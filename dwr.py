import tkinter as tk
from tkinter import messagebox
import time
import threading
import os

def play_sound():
    try:
        os.startfile(r"C:\Users\DELL\Music\MEmu Music\tune 1.mpeg")
    except Exception as e:
        messagebox.showerror("Error", f"Could not play sound:\n{e}")

def show_notification():
    popup = tk.Toplevel()
    popup.title("Reminder")
    popup.geometry("250x100")
    popup.attributes("-topmost", True)
    label = tk.Label(popup, text="💧 Drink Water!", font=("Arial", 14))
    label.pack(expand=True, fill=tk.BOTH)
    popup.after(3000, popup.destroy)  # Auto close in 3 seconds

def start_timer():
    try:
        hrs = int(hours_entry.get())
        mins = int(minutes_entry.get())
        secs = int(seconds_entry.get())
        total_seconds = hrs * 3600 + mins * 60 + secs

        def countdown():
            for remaining in range(total_seconds, 0, -1):
                mins_left, secs_left = divmod(remaining, 60)
                hrs_left, mins_left = divmod(mins_left, 60)
                timer_label.config(text=f"Time Left: {hrs_left:02d}:{mins_left:02d}:{secs_left:02d}")
                time.sleep(1)
            if choice.get() == "Notification":
                show_notification()
            else:
                play_sound()

        threading.Thread(target=countdown, daemon=True).start()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for time.")

# GUI setup
root = tk.Tk()
root.title("Reminder Timer")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Set Time (HH:MM:SS):", font=("Arial", 12)).pack(pady=5)

frame = tk.Frame(root)
frame.pack()

hours_entry = tk.Entry(frame, width=5)
hours_entry.insert(0, "0")
hours_entry.pack(side=tk.LEFT, padx=5)

minutes_entry = tk.Entry(frame, width=5)
minutes_entry.insert(0, "0")
minutes_entry.pack(side=tk.LEFT, padx=5)

seconds_entry = tk.Entry(frame, width=5)
seconds_entry.insert(0, "5")
seconds_entry.pack(side=tk.LEFT, padx=5)

choice = tk.StringVar(value="Notification")
tk.Radiobutton(root, text="Notification", variable=choice, value="Notification").pack()
tk.Radiobutton(root, text="Sound", variable=choice, value="Sound").pack()

tk.Button(root, text="Start Timer", command=start_timer, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

timer_label = tk.Label(root, text="Time Left: 00:00:00", font=("Arial", 12))
timer_label.pack()

root.mainloop()
