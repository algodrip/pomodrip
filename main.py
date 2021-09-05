import tkinter as tk
import time
from tkinter import messagebox

# Create window
root = tk.Tk()
# Title
root.title("PomoDrip")
# Window size
root.geometry("650x200")
# Window background color
root.configure(background="#2D142C")
# Disable resizing of the window
root.resizable(width=False, height=False)

# Constants
FONT = "Arial"
FOREGROUND = "#C72C41"
BACKGROUND = "#510A32"

# --- Timer ---

# Variables
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# Set the values of time to 0
hour.set("00")
minute.set("00")
second.set("00")

# Labels for the hours, minutes, and seconds
hour_text = tk.Label(root, font=(FONT, 12), fg="#EE4540")

# Input for each variable
hour_entry = tk.Entry(root, font=(FONT, 24),
                      textvariable=hour, width=5,
                      fg=FOREGROUND, bg=BACKGROUND,
                      justify="center", bd="0")
hour_entry.place(x=10, y=30)

minute_entry = tk.Entry(root, font=(FONT, 24),
                        textvariable=minute, width=5,
                        fg=FOREGROUND, bg=BACKGROUND,
                        justify="center", bd="0")
minute_entry.place(x=100, y=30)

second_entry = tk.Entry(root, font=(FONT, 24),
                        textvariable=second, width=5,
                        fg=FOREGROUND, bg=BACKGROUND,
                        justify="center", bd="0")
second_entry.place(x=190, y=30)


def time_input():
    '''Converts seconds into hour, minute, and second'''
    timing = 0
    try:
        timing = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except TypeError:
        messagebox.showinfo("Error","Please check your entry.")
    finally:
        if timing == 0 or timing is None:
            messagebox.showinfo("Error", "Enter a Value.")
        else:
            while timing > -1:
                # converts minutes to seconds
                mins, secs = divmod(timing, 60)
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
                if timing == 0:
                    messagebox.showinfo("Timer", "Time's up! 🎊")
                    # sets the timer back to 00 instead of 0
                    hour.set("00")
                    minute.set("00")
                    second.set("00")
                    # resets the window size
                    root.geometry("700x200")
                # subtracts the time
                timing -= 1


# Activation button
button_entry = tk.Button(root, text="Start!", bd="0",
                         command=time_input, width=38,
                         compound="c",
                         fg=FOREGROUND, bg=BACKGROUND)
button_entry.place(x=10, y=75)


def second_entry_clear(en):
    '''Defines timer_entry_clear function'''
    if second_entry.get() == "00" or second_entry.get() == "0":
        second_entry.delete(0, tk.END)


def minute_entry_clear(en):
    if minute_entry.get() == "00" or minute_entry.get() == "0":
        minute_entry.delete(0, tk.END)


def hour_entry_clear(en):
    if hour_entry.get() == "00" or hour_entry.get() == "0":
        hour_entry.delete(0, tk.END)


# Bind the entry boxes
hour_entry.bind("<Button-1>", hour_entry_clear)
minute_entry.bind("<Button-1>", minute_entry_clear)
second_entry.bind("<Button-1>", second_entry_clear)

# --- Todo List ---

# Frame used to separate the to do list
todo_list_frame = tk.Frame(root)
todo_list_frame.place(x=300, y=30)

# Create the actual to do list
todo_list = tk.Listbox(todo_list_frame, width=25,
                       height=7, font=(FONT, 12),
                       bd=0, fg=FOREGROUND,
                       bg=BACKGROUND, activestyle="none") 
todo_list.pack(side=tk.LEFT, fill=tk.BOTH)

# task_list values
task_list = []

# Insert a new task
for item in task_list:
    todo_list.insert(tk.END, item)

# Scroll bar for to do list
todo_list_scroll_bar = tk.Scrollbar(todo_list_frame)
todo_list_scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Control for the scroll bar
todo_list.config(yscrollcommand=todo_list_scroll_bar.set)
todo_list_scroll_bar.config(command=todo_list.yview)

# Create an entry box for the to do list
todo_list_entry = tk.Entry(root, font=(FONT, 12),
                           fg=FOREGROUND, bg=BACKGROUND,
                           bd=1, width=26)
todo_list_entry.place(x=300, y=170)

# Create a frame for the list buttons
list_button_frame = tk.Frame(root)
list_button_frame.place(x=550, y=30)


def new_task():
    '''defines new task'''
    task = todo_list_entry.get()
    if task != "":
        todo_list.insert(tk.END, task)
    else:
        messagebox.showinfo("Error", "Please enter some task.")


def del_task():
    '''defines delete task'''
    todo_list.delete(tk.ANCHOR)


# Insert text into the listbox
addtask_button = tk.Button(list_button_frame, text="Insert",
                           font=(FONT, 12), bd=0,
                           fg=FOREGROUND, bg=BACKGROUND,
                           width=10, command=new_task)
addtask_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

# Delete items in the list
del_task_button = tk.Button(list_button_frame, text="Remove",
                            font=(FONT, 12), bd=0,
                            fg=FOREGROUND, bg=BACKGROUND,
                            width=10, command=del_task)
del_task_button.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

# Loop the window to keep it active
root.mainloop()
