
from msvcrt import setmode
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from tkcalendar import *
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/calendar page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class calendarPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.calendarPage()    

    def calendarPage(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 700,
            width = 1080,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.calendar = Calendar(self.master, setmode="day", date_pattern = 'yyyy-mm-dd')
        self.calendar.pack(pady=145)

        self.open_calendar = Button(self.calendar, text="open to do list") 
        self.open_calendar.pack(padx=15,pady=15)

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            536.0,
            527.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            120.0,
            39.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=682.0,
            y=24.0,
            width=112.0,
            height=22.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=858.0,
            y=24.0,
            width=68.0,
            height=22.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=559.0,
            y=24.0,
            width=47.0,
            height=22.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            203.0,
            357.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            155.0,
            180.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            466.0,
            466.0,
            anchor="nw",
            text="n",
            fill="#585E62",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            558.0,
            493.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            425.0,
            565.0,
            anchor="nw",
            text="22-04-2022",
            fill="#585E62",
            font=("OpenSansRoman Bold", 40 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            169.0,
            140.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            202.0,
            441.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            536.0,
            244.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            867.0,
            359.0,
            image=self.image_image_9
        )

        self.canvas.create_text(
            768.0,
            163.0,
            anchor="nw",
            text="To-Do-1",
            fill="#000000",
            font=("OpenSansRoman Light", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            318.0,
            anchor="nw",
            text="To-Do-2",
            fill="#000000",
            font=("OpenSansRoman Light", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            482.0,
            anchor="nw",
            text="To-Do-3",
            fill="#000000",
            font=("OpenSansRoman Light", 16 * -1)
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            736.0,
            174.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            735.0,
            332.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            736.0,
            493.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = self.canvas.create_image(
            534.0,
            121.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = self.canvas.create_image(
            857.0,
            121.0,
            image=self.image_image_14
        )

        self.canvas.create_rectangle(
            424.0,
            152.0,
            644.0,
            365.0,
            fill="#E1E7EB",
            outline="")

        self.canvas.create_text(
            727.0,
            195.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            352.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            514.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("OpenSansRoman Bold", 16 * -1)
        )

        self.canvas.create_text(
            727.0,
            223.0,
            anchor="nw",
            text="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.canvas.create_text(
            723.0,
            379.0,
            anchor="nw",
            text="BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.canvas.create_text(
            723.0,
            540.0,
            anchor="nw",
            text="CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
            fill="#000000",
            font=("OpenSansRoman Light", 12 * -1)
        )

        self.image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.image_15 = self.canvas.create_image(
            529.0,
            446.0,
            image=self.image_image_15
        )

        self.image_image_16 = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.image_16 = self.canvas.create_image(
            529.0,
            544.0,
            image=self.image_image_16
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=808.0,
            y=275.0,
            width=98.0,
            height=19.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=808.0,
            y=441.0,
            width=98.0,
            height=19.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=808.0,
            y=590.0,
            width=98.0,
            height=19.0
        )
        
    def startPage(self):
        self.mainloop()
