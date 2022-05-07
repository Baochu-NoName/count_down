#!usr/bin/env python3
from tkinter import *

import datetime
import time
from playsound import playsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")

        print("The Set date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            playsound("Dance_Monkey.mp3")
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Timer")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hours format", fg="green", bg="black", font="Arial").place(x=60, y=120)

add_time = Label(clock, text="Hour Min Sec", font=60).place(x=110)

set_your_alarm = Label(clock, text="When to wake up", fg="blue", relief="solid", font=("Helevetica",7, "bold")).place(x=0, y=29)

hour = StringVar()
min  = StringVar()
sec  = StringVar()

hour_time = Entry(clock, textvariable=hour, bg="yellow", width="15").place(x=110, y=30)
min_time = Entry(clock, textvariable=min, bg="yellow", width="15").place(x=150, y=30)
sec_time = Entry(clock, textvariable=sec, bg="yellow", width="15").place(x=200, y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)
clock.mainloop()
