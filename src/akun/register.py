import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/register page")

import sys
sys.path.insert(1, "..")
import pageManager as pm

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#window = Tk()

#window.geometry("1080x700")
#window.configure(bg = "#FFFFFF")

class registerPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.registerPage()

    def registerPage(self):
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

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            533.0,
            387.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            345.0,
            629.0,
            anchor="nw",
            text="Warning",
            fill="#FF0101",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            345.0,
            343.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            389.0,
            anchor="nw",
            text="Birthdate",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            436.0,
            anchor="nw",
            text="Gender",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            488.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            341.0,
            533.0,
            anchor="nw",
            text="City",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            341.0,
            581.0,
            anchor="nw",
            text="Country",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            756.0,
            581.0,
            anchor="nw",
            text="Postal Code",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            111.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            297.0,
            anchor="nw",
            text="Full Name",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            62.0,
            anchor="nw",
            text="New Account",
            fill="#000000",
            font=("Helvetica", 24 * -1)
        )

        self.canvas.create_text(
            345.0,
            248.0,
            anchor="nw",
            text="More Details",
            fill="#000000",
            font=("Helvetica", 24 * -1)
        )

        self.canvas.create_text(
            345.0,
            159.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            345.0,
            207.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            771.0,
            175.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.username
        )
        self.entry_1.place(
            x=554.0,
            y=153.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            646.0,
            595.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.password
        )
        self.entry_2.place(
            x=554.0,
            y=573.0,
            width=184.0,
            height=42.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            938.0,
            595.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.password
        )
        self.entry_3.place(
            x=888.0,
            y=573.0,
            width=100.0,
            height=42.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            771.0,
            547.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.fullname
        )
        self.entry_4.place(
            x=554.0,
            y=525.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            771.0,
            500.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.email
        )
        self.entry_5.place(
            x=554.0,
            y=478.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            771.0,
            453.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.birthdate
        )
        self.entry_6.place(
            x=554.0,
            y=431.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            771.0,
            359.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.gender
        )
        self.entry_7.place(
            x=554.0,
            y=337.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            771.0,
            406.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.address
        )
        self.entry_8.place(
            x=554.0,
            y=384.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            771.0,
            312.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.city
        )
        self.entry_9.place(
            x=554.0,
            y=290.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            771.0,
            127.0,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.country
        )
        self.entry_10.place(
            x=554.0,
            y=105.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            771.0,
            223.0,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.postalCode
        )
        self.entry_11.place(
            x=554.0,
            y=201.0,
            width=434.0,
            height=42.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.origin.loginPage(),
            relief="flat"
        )
        self.button_1.place(
            x=808.0,
            y=629.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            85.0,
            162.0,
            anchor="nw",
            text="Page.",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_text(
            85.0,
            119.0,
            anchor="nw",
            text="Register",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            157.0,
            427.0,
            image=self.image_image_2
        )

    #window.resizable(False, False)
    def startPage(self):
        self.mainloop()
