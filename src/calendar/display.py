"""
    File ini adalah file calendar.py
    File ini berfungsi untuk menampilkan kalender kepada pengguna
"""

from tkinter import * # import tkinker untuk GUI
from tkcalendar import *

form = Tk()

def date_selected():
    date = calendar.get_date()
    display_date = Label(text=date)
    display_date.pack(padx=2,pady=2)

calendar = Calendar(form, setmode = "day", date_pattern = 'd/m/yy')
calendar.pack(padx=15, pady=15)

open_calendar = Button(calendar, text="open to do list", command=date_selected) 
open_calendar.pack(padx=15,pady=15)

form.geometry('1080x700')
form.title("Calendar")
form.configure(bg="white")
form.mainloop()
