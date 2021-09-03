from tkinter import *
import time
from tkinter import messagebox
from timer import *

#creates window
root = Tk()
#title
root.title("PomoDrip")
#window size
root.geometry("300x200")

#Variables
hour = StringVar()
minute = StringVar()
second = StringVar()

#sets the values to 0
hour.set("00")
minute.set("00")
second.set("00")

#Input for each variable
hour_entry = Entry(root, font = ("Arial", 12), textvariable = hour, width = 5)
hour_entry.place(x = 80, y = 20)

minute_entry = Entry(root, font = ("Arial", 12), textvariable = minute, width = 5)
minute_entry.place(x = 130, y = 20)

second_entry = Entry(root, font = ("Arial", 12), textvariable = second, width = 5)
second_entry.place(x = 180, y = 20)

#Converts seconds into hour, minute, and second
def time_input():
	Timing = 0
	try:
		Timing = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except TypeError:
		print("Please check your entry.")
	except Exception as e:
		print(e.message + e.args)
	finally:
		if Timing == 0:
			print("Enter a Value.")
	while Timing > -1:
		#converts minutes to seconds
		mins, secs = divmod(Timing,60)

		#converts hours to minutes
		hours = 0
		if mins > 60:
			hours, mins = divmod(mins,60)

			#displays 2 digits
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		root.update()
		time.sleep(1)

		#time's up display
		if Timing == 0:
			messagebox.showinfo("Timer", "Time's up! 🎊")
			# sets the timer back to 00 instead of 0
			hour.set("00")
			minute.set("00")
			second.set("00")
		#subtracts the time
		Timing -= 1

#Activation button
Button_Entry = Button(root, text = "Start!", bd = "5", command = time_input, width = 20, compound ="c")
Button_Entry.place(x = 70, y = 120)

# loops the window to keep it active
root.mainloop()
