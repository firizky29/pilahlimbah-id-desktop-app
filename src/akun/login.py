import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/login page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

import sys
sys.path.insert(1, "..")
import pageManager as pm

#window = Tk()

#window.geometry("1080x700")
#window.configure(bg = "#FFFFFF")

class loginPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.loginPage()

    def loginPage(self):
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
            font=("Helvetica Bold", 20 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            552.0,
            400.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            196.0,
            422.0,
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
            x=582.0,
            y=533.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            540.0,
            495.0,
            anchor="nw",
            text="Is This Your First Time Here?",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            681.0,
            215.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_1.place(
            x=509.0,
            y=183.0,
            width=344.0,
            height=62.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            681.0,
            337.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_2.place(
            x=509.0,
            y=305.0,
            width=344.0,
            height=62.0
        )

        self.canvas.create_rectangle(
            76.0,
            161.0,
            124.0,
            166.0,
            fill="#FFFFFF",
            outline="")

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
            x=582.0,
            y=410.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            85.0,
            162.0,
            anchor="nw",
            text="Page.",
            fill="#000000",
            font=("Helvetica Bold", 32 * -1)
        )

        self.canvas.create_text(
            85.0,
            119.0,
            anchor="nw",
            text="Login",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_text(
            589.0,
            153.0,
            anchor="nw",
            text="Username/User ID/Email",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            645.0,
            272.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            499.0,
            380.0,
            anchor="nw",
            text="Warning",
            fill="#FF0101",
            font=("Helvetica", 16 * -1)
        )

#window.resizable(False, False)

    def startPage(self):
        self.mainloop()
