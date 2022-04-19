import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/profile page")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

import sys
sys.path.insert(1, "..")
import pageManager as pm

#window = Tk()

#window.geometry("1080x700")
#window.configure(bg = "#FFFFFF")

class profilePage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.profilePage()

    def profilePage(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 700,
            width = 1080,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            36.0,
            24.0,
            anchor="nw",
            text="PilahLimbah.id",
            fill="#000000",
            font=("Helvetica", 20 * -1)
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
            command=lambda: self.origin.calendarPage(),
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
            x=559.0,
            y=24.0,
            width=47.0,
            height=22.0
        )

        self.canvas.create_rectangle(
            36.0,
            78.0,
            370.0,
            674.0,
            fill="#F7F9FA",
            outline="")

        self.canvas.create_text(
            56.0,
            128.0,
            anchor="nw",
            text="Profile.",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_text(
            56.0,
            94.0,
            anchor="nw",
            text="My",
            fill="#000000",
            font=("OpenSansRoman Light", 32 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            202.0,
            459.0,
            image=self.image_image_1
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
            x=591.0,
            y=94.0,
            width=198.0,
            height=42.0
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
            x=384.0,
            y=94.0,
            width=198.0,
            height=42.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            714.0,
            456.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            619.0,
            443.75,
            anchor="nw",
            text="Female",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            443.0,
            anchor="nw",
            text="Gender",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            714.0,
            511.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            619.0,
            497.75,
            anchor="nw",
            text="Indonesia",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            497.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            714.0,
            566.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            619.0,
            553.75,
            anchor="nw",
            text="Indonesia",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            553.0,
            anchor="nw",
            text="City",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            574.0,
            619.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            619.0,
            607.75,
            anchor="nw",
            text="Indonesia",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            607.0,
            anchor="nw",
            text="Country",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            895.0,
            619.0,
            image=self.image_image_6
        )

        self.canvas.create_text(
            931.0,
            607.0,
            anchor="nw",
            text="40132",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            775.0,
            608.0,
            anchor="nw",
            text="Postal Code",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            714.0,
            401.0,
            image=self.image_image_7
        )

        self.canvas.create_text(
            619.0,
            391.0,
            anchor="nw",
            text="01-01-1995",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            391.0,
            anchor="nw",
            text="Birthdate",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            714.0,
            346.0,
            image=self.image_image_8
        )

        self.canvas.create_text(
            619.0,
            335.0,
            anchor="nw",
            text="Member (Until ...)",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            335.0,
            anchor="nw",
            text="Role",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=931.0,
            y=652.0,
            width=118.0,
            height=22.0
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            714.0,
            181.0,
            image=self.image_image_9
        )

        self.canvas.create_text(
            619.0,
            176.0,
            anchor="nw",
            text="abcd125",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            175.0625,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            714.0,
            291.0,
            image=self.image_image_10
        )

        self.canvas.create_text(
            619.0,
            282.0,
            anchor="nw",
            text="abcdefg@gmail.com",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            421.0,
            282.0,
            anchor="nw",
            text="Email Address",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            714.0,
            236.0,
            image=self.image_image_11
        )

        self.canvas.create_text(
            619.0,
            227.75,
            anchor="nw",
            text="qwerty9876",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            424.0,
            226.0,
            anchor="nw",
            text="Full Name",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )
    #window.resizable(False, False)
        
    def startPage(self):
        self.mainloop()
