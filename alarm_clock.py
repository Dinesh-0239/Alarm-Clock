"""
This is the Python project on "Alarm Clock" created by Dinesh Singh of BCA Sem-VI from University of Allahabad
Very thankful to Sync Intern's for providing such an amazing opportunity to build this project

"""

#Importing all essential libraries
from tkinter import *
from PIL import Image,ImageTk
import time
from datetime import date
from threading import *
from playsound import playsound

#Method to show the current time
def show_time():
    """Method to display current time"""
    global curr_time
    curr_time = time.strftime("%H:%M:%S")
    current_time.config(text=curr_time)
    current_time.after(100,show_time)    

#Method to reset the clock for alarm
def reset():
    """Method to reset the clock for alarm"""
    alarm_clock_window.title("Alarm Clock--------Alarm time is Reset")
    global hrs,mnts,sec
    hrs.set(hours[0])
    mnts.set(minutes[0])
    sec.set(seconds[0])

#Method to display current time
def show_date():
    """Method to show current date"""
    curr_date = date.today()
    current_date.config(text=curr_date)
    current_date.after(100,show_date)

#Thred to handle infinite loop of the activate alarm method
def Threading():
    """Method to handle the infinite loop of the activate alarm method"""
    alarm = Thread(target=activate_alarm)
    alarm.start()

#Method for set alarm and play music
def activate_alarm():
    """Method for set alarm and play music"""
    alarm_clock_window.title("Alarm Clock--------Alarm is Activated")
    while True:
        set_alarm = f"{hrs.get()}:{mnts.get()}:{sec.get()}"
        if set_alarm == curr_time:
            playsound("alarm_sound.mp3")
            break

#Creating window
alarm_clock_window = Tk()
alarm_clock_window.geometry("550x350")
alarm_clock_window.resizable(False,False)
alarm_clock_window.iconbitmap("appicon.ico")
alarm_clock_window.title("Alarm Clock")
alarm_clock_window.config(bg="light green")

#Display title of the window
Label(alarm_clock_window,text="Alarm Clock",fg="dark red",bg="linen",font=("timesnewroman",24,"bold","underline"),padx=5,pady=5,relief=RAISED).place(x=180,y=20)

#Creating frame for all widgets
clock_frame = LabelFrame(alarm_clock_window,text="Clock",font=("timesnewroman",14,"bold"),labelanchor=SE,height=250,width=300,bg="orange")
clock_frame.place(x=10,y=80)

#Display clock image
clock_img = ImageTk.PhotoImage(Image.open("clock_image.jpg").resize((200,250)))
clock_image = Label(alarm_clock_window,image=clock_img,relief=RAISED)
clock_image.place(x=330,y=80)

#Label for current time
Label(clock_frame,font=("timesnewroman",16,"bold"),fg="red",bg="white",relief=RAISED,text="Current Time:- ").place(x=10,y=20)
current_time= Label(clock_frame,font=("timesnewroman",16,"bold"),fg="red",bg="white",relief=RAISED)
current_time.place(x=190,y=20)

#Invoke method to show current time
show_time()

#Label for current date
Label(clock_frame,font=("timesnewroman",16,"bold"),fg="red",bg="white",relief=RAISED,text="Current Date:- ").place(x=10,y=60)
current_date= Label(clock_frame,font=("timesnewroman",16,"bold"),fg="red",bg="white",relief=RAISED)
current_date.place(x=180,y=60)

#Invoke method to show current date
show_date()

#Label to show "Set Alarm"
Label(clock_frame,font=("timesnewroman",18,"bold"),fg="red",bg="white",relief=RAISED,text="Set Alarm").place(x=100,y=105)

#Label to show "Time"
Label(clock_frame,font=("timesnewroman",16,"bold"),fg="red",bg="white",relief=RAISED,text="Time").place(x=10,y=150)

#Creating and placing dropdown menu for hours in the clock frame
hrs = StringVar(clock_frame)
hours = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
hrs.set(hours[0])
set_hours = OptionMenu(clock_frame,hrs,*hours)
set_hours.place(x=100,y=150)

#Creating and placing dropdown menu for minutes in the clock frame
mnts = StringVar(clock_frame)
minutes = hours 
for value in range(24,60):
    minutes.append(str(value))
mnts.set(minutes[0])
set_minute = OptionMenu(clock_frame,mnts,*minutes)
set_minute.place(x=160,y=150)

#Creating and placing dropdown menu for seconds in the clock frame
sec = StringVar(alarm_clock_window)
seconds = minutes
sec.set(seconds[0])
set_second = OptionMenu(clock_frame,sec,*seconds)
set_second.place(x=220,y=150)

#Button to activate alarm
Button(clock_frame,text="Activate",font=("timesnewroman",12,"bold"),bg="black",fg="white",relief=RAISED,command=Threading).place(x=10,y=190)

#Button to reset time for alarm
Button(clock_frame,text="Reset",font=("timesnewroman",12,"bold"),bg="black",fg="white",relief=RAISED,command=reset).place(x=230,y=190)

alarm_clock_window.mainloop()
