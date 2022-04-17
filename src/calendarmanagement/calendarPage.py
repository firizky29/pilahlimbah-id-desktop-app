
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/calendar page")

import sys
sys.path.insert(1, "..")
import pageManager as pm

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class calendarPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__Init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.calendarPage()    

    def calendarPage(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=700,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            383.0,
            418.0,
            690.0,
            636.0,
            fill="#D2F0FF",
            outline="")

        self.canvas.create_text(
            36.0,
            24.0,
            anchor="nw",
            text="PilahLimbah.id",
            fill="#000000",
            font=("Helvetica", 20 * -1, "bold")
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
            image = self.button_image_2,
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

        self.canvas.create_rectangle(
            36.0,
            78.0,
            370.0,
            636.0,
            fill="#F7F9FA",
            outline="")

        self.canvas.create_text(
            61.0,
            165.0,
            anchor="nw",
            text="I do?",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            466.0,
            466.0,
            anchor="nw",
            text="n",
            fill="#585E62",
            font=("Helvetica", 40 * -1, "bold")
        )

        self.canvas.create_text(
            515.0,
            466.0,
            anchor="nw",
            text="task",
            fill="#000000",
            font=("Helvetica", 40 * -1, "bold")
        )

        self.canvas.create_text(
            425.0,
            565.0,
            anchor="nw",
            text="22-04-2022",
            fill="#585E62",
            font=("Helvetica", 40 * -1, "bold")
        )

        self.canvas.create_text(
            61.0,
            125.0,
            anchor="nw",
            text="What should",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_rectangle(
            93.0,
            303.0,
            312.0,
            580.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            383.0,
            82.0,
            690.0,
            406.0,
            fill="#10429A",
            outline="")

        self.canvas.create_rectangle(
            703.0,
            82.0,
            1032.0,
            636.0,
            fill="#F2EFF9",
            outline="")

        self.canvas.create_text(
            768.0,
            163.0,
            anchor="nw",
            text="To-Do-1",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            318.0,
            anchor="nw",
            text="To-Do-2",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            482.0,
            anchor="nw",
            text="To-Do-3",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            736.0,
            174.0,
            image=self.image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            735.0,
            332.0,
            image=self.image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            736.0,
            493.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            457.0,
            105.0,
            anchor="nw",
            text="Calendar",
            fill="#FFFFFF",
            font=("Helvetica", 24 * -1, "bold")
        )

        self.canvas.create_text(
            780.0,
            105.0,
            anchor="nw",
            text="To Do List",
            fill="#000000",
            font=("Helvetica", 24 * -1)
        )

        self.canvas.create_rectangle(
            424.0,
            152.0,
            644.0,
            365.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            727.0,
            195.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            352.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            514.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="Not Done",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="Done",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            727.0,
            223.0,
            anchor="nw",
            text="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            723.0,
            379.0,
            anchor="nw",
            text="BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            723.0,
            540.0,
            anchor="nw",
            text="CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            483.0,
            435.0,
            anchor="nw",
            text="You have ",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            493.0,
            534.0,
            anchor="nw",
            text="on",
            fill="#000000",
            font=("Helvetica", 20 * -1)
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
        