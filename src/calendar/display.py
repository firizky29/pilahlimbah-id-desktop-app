"""
    File ini adalah file calendar.py
    File ini berfungsi untuk menampilkan kalender kepada pengguna
"""

from tkinter import * # import tkinker untuk GUI
from tkcalendar import *
import mysql.connector

form = Tk()

def date_selected():
    mysqldb = mysql.connector.connect(host="pilahlimbah.mariadb.database.azure.com", user="pilahlimbah@pilahlimbah", password="BDDL&g38Mv", database = "pilahlimbahid")
    date = calendar.get_date()
    display_date = Label(text=date)
    display_date.pack(padx=2,pady=2)
    sqlcursor = mysqldb.cursor()
    sqlcursor.execute("SELECT * FROM task")
    for i in sqlcursor:
        if str(i[0]) == str(date):
            print(i[2])
            display_task = Label(text=i[2])
            display_task.pack(padx=2,pady=2)

calendar = Calendar(form, setmode = "day", date_pattern = 'yyyy-mm-dd')
calendar.pack(padx=100, pady=100)
# calendar.configure(color = "blue")

open_calendar = Button(calendar, text="open to do list", command=date_selected) 
open_calendar.pack(padx=15,pady=15)

form.geometry('1440x1024')
form.title("Calendar")
form.configure(bg="cyan")
form.mainloop()
