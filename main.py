import tkinter as tk
import time
from tkinter import messagebox

# creates window
root = tk.Tk()
# Title
root.title("PomoDrip")
# window size
root.geometry("300x200")
# window background color
root.configure(background="#010114")

''' Experimental code (testing out how to create a custom title and menu bar)

# Defines drag movement
def drag_movement(drag):
	root.geometry(f'+{drag.x_root}+{drag.y_root}')

# remove title bar
root.overrideredirect(True)

# creates fake title bar
title_bar = tk.Frame(root, bg = "#010114", relief = "raised", bd = 0)
title_bar.pack(side = tk.TOP, expand = 1, fill = tk.BOTH)

#title text
title_label = tk.Label(title_bar, text = " PomoDrip", font = ("Arial", 10), bg = "#010114", fg = "#ffa500")
title_label.place(x = 0, y = 0)

#creates title bar close button
title_button_close = tk.Button(title_bar, text = "  x  ", font = ("Arial", 12), bd = 0, bg = "#010114", fg = "#ffa500", command = root.destroy)

# places title bar close button
title_button_close.place(x = 260, y = 0)

!!!WARNING!!! This line of code does not function while root.overridedirect is set to True


#creates a minimize button
title_button_minimize = tk.Button(title_bar, text = "  _  ", font = ("Arial", 12), bd = 0, bg = "#010114", fg = "#ffa500", command = lambda: root.wm_state("iconic"))
# places title bar minimize button
title_button_minimize.place(x = 230, y = 0)

!!!WARNING!!!


#Binds the title bar (allows it to be dragged)
title_bar.bind("<B1-Motion>", drag_movement)
title_label.bind("<B1-Motion>", drag_movement)
'''

# Variables
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# sets the values to 0
hour.set("00")
minute.set("00")
second.set("00")

# Input for each variable
hour_entry = tk.Entry(root, font = ("Arial", 12), textvariable = hour, width = 5, bg = "#010114", fg = "#ffa500")
hour_entry.place(x = 80, y = 40)

minute_entry = tk.Entry(root, font = ("Arial", 12), textvariable = minute, width = 5, bg = "#010114", fg = "#ffa500")
minute_entry.place(x = 130, y = 40)

second_entry = tk.Entry(root, font = ("Arial", 12), textvariable = second, width = 5, bg = "#010114", fg = "#ffa500")
second_entry.place(x = 180, y = 40)


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
		else:
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

				# Updates the numbers displayed in the entrybox
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
				# resizes the window
				root.geometry("300x200")
# Activation button
Button_Entry = tk.Button(root, text = "Start!", bd = "5", command = time_input, width = 20, compound = "c", bg = "#010114", fg = "#ffa500")
Button_Entry.place(x = 70, y = 120)

# Defines timer_entry_clear function
def second_entry_clear(dele):
	if second_entry.get() == "00" or second_entry.get() == "0":
		second_entry.delete(0, tk.END)

def minute_entry_clear(dele):
	if minute_entry.get() == "00" or minute_entry.get() == "0":
		minute_entry.delete(0, tk.END)

def hour_entry_clear(dele):
	if hour_entry.get() == "00" or hour_entry.get() == "0":
		hour_entry.delete(0, tk.END)

# Binds the entry boxes
hour_entry.bind("<Button-1>", hour_entry_clear)
minute_entry.bind("<Button-1>", minute_entry_clear)
second_entry.bind("<Button-1>", second_entry_clear)

#create a textbox

#quote_messages = tk.label("")


# loops the window to keep it active
root.mainloop()
