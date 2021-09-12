'''PomoDrip: Pomodoro Timer by the Algo Drip team
   Keep track of your tasks with 25 minute work sessions and 5 minute breaks!
'''
import tkinter as tk
import time
from tkinter import messagebox
from tkinter import ttk
from sys import argv

# Constants
TITLE = "PomoDrip"
FONT = "Arial"
BACKGROUND = "#2D142C"
ENTRY_FOREGROUND = "#C72C41"
ENTRY_BACKGROUND = "#510A32"
FONT_SIZE_ENTRIES = 24
FONT_SIZE_TODO = 12

# Create window
root = tk.Tk()

# --- TIME VARIABLES ---

# work
hour_work = tk.StringVar()
minute_work = tk.StringVar()
second_work = tk.StringVar()
# rest
hour_rest = tk.StringVar()
minute_rest = tk.StringVar()
second_rest = tk.StringVar()

# create tabs
tab_frame = ttk.Notebook(root)
tab_frame.pack(side=tk.LEFT)

# tab designation
tab_frame_1 = tk.Frame(tab_frame, width=300, height=200, bg=BACKGROUND)
tab_frame_1.pack(fill=tk.BOTH, expand=1)

tab_frame_2 = tk.Frame(tab_frame, width=300, height=200, bg=BACKGROUND)
tab_frame_2.pack(fill=tk.BOTH, expand=1)

# show tabs
tab_frame.add(tab_frame_1, text="Timer")
tab_frame.add(tab_frame_2, text="Progress")

# Input for each time variable

# work
hour_entry_work = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                           textvariable=hour_work, width=5,
                           fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                           justify="center", bd="0")
hour_entry_work.place(x=10, y=30)

minute_entry_work = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                             textvariable=minute_work, width=5,
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                             justify="center", bd="0")
minute_entry_work.place(x=100, y=30)

second_entry_work = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                             textvariable=second_work, width=5,
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                             justify="center", bd="0")
second_entry_work.place(x=190, y=30)

# rest
hour_entry_rest = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                           textvariable=hour_rest, width=5,
                           fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                           justify="center", bd="0")
hour_entry_rest.place(x=10, y=75)

minute_entry_rest = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                             textvariable=minute_rest, width=5,
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                             justify="center", bd="0")
minute_entry_rest.place(x=100, y=75)

second_entry_rest = tk.Entry(tab_frame_1, font=(FONT, FONT_SIZE_ENTRIES),
                             textvariable=second_rest, width=5,
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                             justify="center", bd="0")
second_entry_rest.place(x=190, y=75)

# Initialize necessary todo list variables
todo_list_frame = tk.Frame(root)
todo_list = tk.Listbox(todo_list_frame, width=25,
                       height=7, font=(FONT, FONT_SIZE_TODO),
                       bd=0, fg=ENTRY_FOREGROUND,
                       bg=ENTRY_BACKGROUND, activestyle="none")
# Create an entry box for the todo list
todo_list_entry = tk.Entry(root, font=(FONT, FONT_SIZE_TODO),
                           fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                           bd=1, width=26)


def time_input_rest():
    '''Get the values from the hour, minute and seconds entries.
    If the inputted values are correct, start the timer,
    notifying the user when it finishes.
    '''
    timing_rest = 0

    try:
        timing_rest = int(hour_rest.get())*3600 + int(minute_rest.get())*60 + int(second_rest.get())

    except TypeError:
        messagebox.showinfo("Error", "Please check your entry.")

    finally:

        if timing_rest == 0 or timing_rest is None:
            messagebox.showinfo("Error", "Enter a value.")

        else:
            while timing_rest > -1:

                # Convert minutes to seconds
                mins_rest, secs_rest = divmod(timing_rest, 60)
                # Resize the window
                root.geometry("300x200")
                # Convert hours to minutes
                hrs_rest = 0
                if mins_rest > 60:
                    hours, mins = divmod(mins_rest, 60)

                # Display 2 digits
                hour_work.set("{0:2d}".format(hrs_rest))
                minute_work.set("{0:2d}".format(mins_rest))
                second_work.set("{0:2d}".format(secs_rest))

                # Update the numbers displayed in the entrybox
                root.update()
                time.sleep(1)

                # Time's up display
                if timing_rest == 0:
                    messagebox.showinfo("Timer", "Time's up! 🎊")
                    # Set the timer back to 00 instead of 0
                    hour_rest.set("00")
                    minute_rest.set("00")
                    second_rest.set("00")
                    # Resets the window size
                    root.geometry("650x200")

                # Subtract the time
                timing_rest -= 1


def time_input_work():
    '''Get the values from the hour, minute and seconds entries.
    If the inputted values are correct, start the timer,
    notifying the user when it finishes.
    '''
    timing_work = 0

    try:
        timing_work = int(hour_work.get())*3600 + int(minute_work.get())*60 + int(second_work.get())

    except TypeError:
        messagebox.showinfo("Error", "Please check your entry.")

    finally:

        if timing_work == 0 or timing_work is None:
            messagebox.showinfo("Error", "Enter a value.")

        else:
            while timing_work > -1:

                # Convert minutes to seconds
                mins_work, secs_work = divmod(timing_work, 60)
                # Resize the window
                root.geometry("300x200")
                # Convert hours to minutes
                hrs_work = 0
                if mins_work > 60:
                    hrs_work, mins_work = divmod(mins_work, 60)

                # Display 2 digits
                hour_work.set("{0:2d}".format(hrs_work))
                minute_work.set("{0:2d}".format(mins_work))
                second_work.set("{0:2d}".format(secs_work))

                # Update the numbers displayed in the entrybox
                root.update()
                time.sleep(1)

                # Time's up display
                if timing_work == 0:
                    # Set the timer back to 00 instead of 0
                    hour_work.set("00")
                    minute_work.set("00")
                    second_work.set("00")
                    # calculates rest
                    time_input_rest()
                # Subtract the time
                timing_work -= 1


def second_entry_clear_work(en):
    '''Clear the second entry if it reaches zero'''
    if second_entry_work.get() == "00" or second_entry_work.get() == "0":
        second_entry_work.delete(0, tk.END)


def second_entry_clear_rest(en):    
    if second_entry_rest.get() == "00" or second_entry_rest.get() == "0":
        second_entry_rest.delete(0, tk.END)


def minute_entry_clear_work(en):
    '''Clear the minute entry if it reaches zero'''
    if minute_entry_work.get() == "00" or minute_entry_work.get() == "0":
        minute_entry_work.delete(0, tk.END)


def minute_entry_clear_rest(en):    
    if minute_entry_rest.get() == "00" or minute_entry_rest.get() == "0":
        minute_entry_rest.delete(0, tk.END)


def hour_entry_clear_work(en):
    '''Clear the hour entry if it reaches zero'''
    if hour_entry_work.get() == "00" or hour_entry_work.get() == "0":
        hour_entry_work.delete(0, tk.END)


def hour_entry_clear_rest(en):    
    if hour_entry_rest.get() == "00" or hour_entry_rest.get() == "0":
        hour_entry_rest.delete(0, tk.END)


def new_task():
    '''Add a new task to the todo list'''
    task = todo_list_entry.get()
    if task != "":
        todo_list.insert(tk.END, task)
    else:
        messagebox.showinfo("Error", "Please enter some task.")


def del_task():
    '''Delete a task from the todo list'''
    todo_list.delete(tk.ANCHOR)


def main():
    '''
    ===== SETUP APPLICATION ======
    '''

    # Title
    root.title(TITLE)
    # Window size
    root.geometry("650x200")
    # Window background color
    root.configure(background=BACKGROUND)
    # Disable resizing of the window
    root.resizable(width=False, height=False)

    # Parse args

    # Help
    if "--help" in argv:
        print(r"  _____                      _____       _       ")
        print(r" |  __ \                    |  __ \     (_)      ")
        print(r" | |__) |__  _ __ ___   ___ | |  | |_ __ _ _ __  ")
        print(r" |  ___/ _ \| '_ ` _ \ / _ \| |  | | '__| | '_ \ ")
        print(r" | |  | (_) | | | | | | (_) | |__| | |  | | |_) |")
        print(r" |_|   \___/|_| |_| |_|\___/|_____/|_|  |_| .__/ ")
        print(r"                                          | |    ")
        print(r"                                          |_|    ")
        print("")
        print("usage: pomodrip [--todolist]")
        print("")
        print("PomoDrip is a tkinter-based Pomodoro Timer written in Python.")
        print("")
        print("OPTIONS:")
        print("   --todolist   Enable a todo-list (EXPERIMENTAL)")
        print("")
        print("")
        print("Report bugs to https://github.com/algodrip/pomodrip/issues")
        return

    # Activate Todo list
    show_todo_list = bool("--todolist" in argv)

    # --- TIMER ---

    # Set the values of time to 0
    hour_work.set("00")
    minute_work.set("00")
    second_work.set("00")
    
    hour_rest.set("00")
    minute_rest.set("00")
    second_rest.set("00")

    # Labels for the hours, minutes, and seconds
    # -- Unused so we are commenting it out for now
    # hour_text = tk.Label(root, font=(FONT, FONT_SIZE_TODO), fg="#EE4540")

    # Button to activate the timer
    button_entry = tk.Button(tab_frame_1, text="Start!", bd="0",
                             command=time_input_work, width=38,
                             compound="c",
                             fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND)
    button_entry.place(x=10, y=105)

    # Bind the entry boxes
    hour_entry_work.bind("<Button-1>", hour_entry_clear_work)
    minute_entry_work.bind("<Button-1>", minute_entry_clear_work)
    second_entry_work.bind("<Button-1>", second_entry_clear_work)
    hour_entry_rest.bind("<Button-1>", hour_entry_clear_rest)
    minute_entry_rest.bind("<Button-1>", minute_entry_clear_rest)
    second_entry_rest.bind("<Button-1>", second_entry_clear_rest)

    # --- TO-DO LIST ---

    if show_todo_list:
        # Frame used to separate the todo list
        todo_list_frame.place(x=300, y=30)

        # Create the actual todo list
        todo_list.pack(side=tk.LEFT, fill=tk.BOTH)

        # task_list values
        task_list = []

        # Insert a new task
        for item in task_list:
            todo_list.insert(tk.END, item)

        # Scroll bar for todo list
        todo_list_scroll_bar = tk.Scrollbar(todo_list_frame)
        todo_list_scroll_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Control for the scroll bar
        todo_list.config(yscrollcommand=todo_list_scroll_bar.set)
        todo_list_scroll_bar.config(command=todo_list.yview)

        todo_list_entry.place(x=300, y=170)

        # Create a frame for the list buttons
        list_button_frame = tk.Frame(root)
        list_button_frame.place(x=550, y=30)

        # Insert text into the listbox
        addtask_button = tk.Button(list_button_frame, text="Insert",
                                   font=(FONT, FONT_SIZE_TODO), bd=0,
                                   fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                                   width=10, command=new_task)
        addtask_button.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # Delete items in the list
        del_task_button = tk.Button(list_button_frame, text="Remove",
                                    font=(FONT, FONT_SIZE_TODO), bd=0,
                                    fg=ENTRY_FOREGROUND, bg=ENTRY_BACKGROUND,
                                    width=10, command=del_task)
        del_task_button.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)

    # Loop the window
    root.mainloop()


if __name__ == "__main__":
    main()
