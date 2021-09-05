import tkinter as tk
import time
from tkinter import messagebox

# creates window
root = tk.Tk()
# title
root.title("PomoDrip")
# window size
root.geometry("700x200")
# window background color
root.configure(background="#120130")
#disables resizing of the window
root.resizable(width=False, height=False)

# Variables
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# sets the values to 0
hour.set("00")
minute.set("00")
second.set("00")

# Input for each variable
hour_entry = tk.Entry(root, font = ("Arial", 24)
		, textvariable = hour, width = 5
		, fg = "#059fb0", bg = "#1b0248"
		, justify="center", bd = "0")
hour_entry.place(x = 10, y = 30)

minute_entry = tk.Entry(root, font = ("Arial", 24)
		, textvariable = minute, width = 5
		, fg = "#059fb0", bg = "#1b0248"
		, justify="center", bd = "0")
minute_entry.place(x = 100, y = 30)

second_entry = tk.Entry(root, font = ("Arial", 24)
		, textvariable = second, width = 5
		, fg = "#059fb0", bg = "#1b0248"
		, justify="center", bd = "0")
second_entry.place(x = 190, y = 30)


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
				# resizes the window
				root.geometry("300x200")
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
					# resets the window size
					root.geometry("700x200")
				# subtracts the time
				Timing -= 1

# Activation button
Button_Entry = tk.Button(root, text = "Start!", bd = "0"
		, command = time_input, width = 38
		, compound = "c"
		, fg = "#FD9A24", bg = "#1b0248")
Button_Entry.place(x = 10, y = 75)

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

# frame used to separate the to do list
to_do_list_frame = tk.Frame(root)
to_do_list_frame.place(x = 400, y = 30)

# creating the actual to do list
To_do_list = tk.Listbox(to_do_list_frame, width = 25
		, height = 8, font = ("Arial", 12)
		, bd = 0, fg = "#059fb0"
		, bg = "#1b0248", activestyle = "none") 
To_do_list.pack(side = tk.LEFT, fill = tk.BOTH)

# task_list values
task_list = [
	"do school work",
	"finish this project",
	"anime",
]

# inserting a new task
for item in task_list:
	To_do_list.insert(tk.END, item)

# scroll bar for to do list
to_do_list_scroll_bar = tk.Scrollbar(to_do_list_frame)
to_do_list_scroll_bar.pack(side = tk.RIGHT, fill = tk.BOTH)

# controls for the scroll bar
To_do_list.config(yscrollcommand = to_do_list_scroll_bar.set)
to_do_list_scroll_bar.config(command = To_do_list.yview)

# creates an entry box for the to do list
to_do_list_entry = tk.Entry(root, font = ("Arial", 12)
		, fg = "#059fb0", bg = "#1b0248"
		, bd = 0)
to_do_list_entry.place(x = 10, y = 110)

# creates a frame for the list buttons
list_button_frame = tk.Frame(root)
list_button_frame.place(x = 10, y = 140)

# defines new task
def new_task():
	task = to_do_list_entry.get()
	if task != "": 
		To_do_list.insert(tk.END, task)
	else:
		messagebox("Error", "Please enter some task.")

# defines delete task
def del_task():
    To_do_list.delete(tk.ANCHOR) 

# inserts text into the listbox
addtask_button = tk.Button(list_button_frame, text = "Insert"
		, font = ("Arial", 12), bd = 0
		, fg = "#059fb0", bg = "#1b0248"
		, command = new_task)
addtask_button.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)

# deletes items in the list 
del_task_button = tk.Button(list_button_frame, text = "Remove"
		, font = ("Arial", 12), bd = 0
		, fg = "#059fb0", bg = "#1b0248"
		, command = del_task)
del_task_button.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)

# loops the window to keep it active
root.mainloop()
