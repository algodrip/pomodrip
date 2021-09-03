import tkinter as tk
import time
from tkinter import messagebox
from timer import *

# creates window
root = tk.Tk()
# title
root.title("PomoDrip")
# window size
root.geometry("300x200")

# Variables
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# sets the values to 0
hour.set("00")
minute.set("00")
second.set("00")

# Input for each variable
hour_entry = tk.Entry(root, font = ("Arial", 12), textvariable = hour, width = 5)
hour_entry.place(x = 80, y = 20)

minute_entry = tk.Entry(root, font = ("Arial", 12), textvariable = minute, width = 5)
minute_entry.place(x = 130, y = 20)

second_entry = tk.Entry(root, font = ("Arial", 12), textvariable = second, width = 5)
second_entry.place(x = 180, y = 20)

# Converts seconds into hour, minute, and second
def time_input():
	Timing = 0
	try:
		Timing = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except TypeError:
		messagebox.showinfo("Error","Please check your entry.")
	finally:
		if Timing == 0 or Timing is None:
			messagebox.showinfo("Error", "Enter a Value.")
	while Timing > -1:
		# converts minutes to seconds
		mins, secs = divmod(Timing, 60)

		# converts hours to minutes
		hours = 0
		if mins > 60:
			hours, mins = divmod(mins, 60)

			# displays 2 digits
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		root.update()
		time.sleep(1)

		# time's up display
		if Timing == 0:
			messagebox.showinfo("Timer", "Time's up! 🎊")
			# sets the timer back to 00 instead of 0
			hour.set("00")
			minute.set("00")
			second.set("00")
		# subtracts the time
		Timing -= 1

# Activation button
Button_Entry = tk.Button(root, text = "Start!", bd = "5", command = time_input, width = 20, compound = "c")
Button_Entry.place(x = 70, y = 120)

# Defines timer_entry_clear function
def second_entry_clear(en):
	if second_entry.get() == "00" or second_entry.get() == "0":
		second_entry.delete(0, tk.END)

def minute_entry_clear(en):
	if minute_entry.get() == "00" or minute_entry.get() == "0":
		minute_entry.delete(0, tk.END)

def hour_entry_clear(en):
	if hour_entry.get() == "00" or hour_entry.get() == "0":
		hour_entry.delete(0, tk.END)

# Binds the entry boxes
hour_entry.bind("<Button-1>", hour_entry_clear)
minute_entry.bind("<Button-1>", minute_entry_clear)
second_entry.bind("<Button-1>", second_entry_clear)

# loops the window to keep it active
root.mainloop()
