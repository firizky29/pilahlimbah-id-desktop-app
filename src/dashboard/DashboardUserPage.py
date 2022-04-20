
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/dashboard page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DashboardUserPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.DashboardUserPage()
        
    def DashboardUserPage(self):
        content_list = []
        title_list = []
        content = self.origin.mydb.cursor()
        content.execute("select * from content")
        for (i, t, c) in content.fetchall():
            title_list.append(t)
            content_list.append(c)
        content_index = 0
        
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
            font=("Helvetica", 20 * -1, "bold")
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_1 = Button(
            image= self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg="white"
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
            image= self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_2.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_3 = Button(
            image= self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_3.place(
            x=414.0,
            y=584.0,
            width=160.0,
            height=60.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_4 = Button(
            image= self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_4.place(
            x=872.0,
            y=584.0,
            width=160.0,
            height=60.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_5 = Button(
            image= self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_5.place(
            x=858.0,
            y=24.0,
            width=68.0,
            height=22.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_6 = Button(
            image= self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_6.place(
            x=559.0,
            y=24.0,
            width=47.0,
            height=22.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_7 = Button(
            image= self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat",
            bg="white"
        )
        self.button_7.place(
            x=559.0,
            y=24.0,
            width=47.0,
            height=22.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            203.0,
            376.0,
            image= self.image_image_1
        )

        self.canvas.create_text(
            56.0,
            128.0,
            anchor="nw",
            text="PilahLimbah.id!",
            fill="#FFFFFF",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            56.0,
            94.0,
            anchor="nw",
            text="Welcome to",
            fill="#FFFFFF",
            font=("Helvetica", 32 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_2 = self.canvas.create_image(
            718.0,
            325.0,
            image= self.image_image_2
        )

        self.canvas.create_text(
            444.0,
            154.0,
            anchor="nw",
            text=content_list[content_index],
            fill="#000000",
            font=("Helvetica", 24 * -1)
        )

        self.canvas.create_text(
            444.0,
            109.0,
            anchor="nw",
            text=title_list[content_index],
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            662.0,
            597.0,
            anchor="nw",
            text=f"{content_index+1}/{len(content_list)}",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            203.0,
            460.0,
            image= self.image_image_3
        )
    
    def startPage(self):
        self.mainloop()
