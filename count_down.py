from tkinter import *

import time
from playsound import playsound

def set_timer(hour_time, min_time, sec_time):

    hour_number = int(hour_time)
    min_number = int(min_time)
    sec_number = int(sec_time)

    while True:
        time.sleep(1)
        
        if sec_number > 0:
            sec_number -= 1
        elif  sec_number == 0 and min_number > 0:
            sec_number = 59
            min_number -=1
        elif min_number == 0 and sec_number == 0 and hour_number > 0:
            sec_number = 59
            min_number = 59
            hour_number -=1
        elif  hour_number == 0 and min_number == 0 and sec_number == 0:
            print("Time is up!")
            playsound("Dance_Monkey.mp3") # Your python file and .mp3 file must be in the same folder
            break

        print(hour_number, min_number, sec_number)

        

def run_timer():
    hour_time = f"{hour.get()}"
    min_time = f"{min.get()}"
    sec_time = f"{sec.get()}"
    set_timer(hour_time, min_time, sec_time)

count_down = Tk()

hour = StringVar()
min  = StringVar()
sec  = StringVar()

count_down.title("Count down timer")
count_down.geometry("400x200")

format_time = Label(count_down, text="HOUR MINUTE SECOND").place(x=110)

hour_input = Entry(count_down, textvariable=hour, fg="green", width=20).place(x=110, y=30)
min_input = Entry(count_down, textvariable=min, fg="green", width=20).place(x=150, y=30)
sec_input = Entry(count_down, textvariable=sec, fg="green", width=20).place(x=200, y=30)

submit = Button(count_down, text="Set Time", fg="red", width=10, command=run_timer).place(x=110, y=100)


count_down.mainloop()
