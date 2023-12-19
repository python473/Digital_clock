import tkinter
import time


def set_clock():
    time_str = (time.strftime("%I:%M:%S %p"))
    time_label.config(text=time_str)
    time_label.after(1000, set_clock)
    day_str = (time.strftime("%A"))
    day_label.config(text=day_str)
    date_str = time.strftime("%B %d, %Y")
    date_label.config(text=date_str)


window = tkinter.Tk()
window.title("Digital Clock")


time_label = tkinter.Label(window, font=("Times New Roman",50), fg="red", bg="black", borderwidth=20)
time_label.pack()
day_label = tkinter.Label(window, font=("cormorant",20), fg="black")
day_label.pack()
date_label = tkinter.Label(window, font=("Arial",20), fg="black")
date_label.pack()
set_clock()
window.mainloop()
