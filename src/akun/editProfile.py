import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/edit profile page")

import sys
sys.path.insert(1, "..")
import pageManager as pm

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#window = Tk()

#window.geometry("1080x700")
#window.configure(bg = "#FFFFFF")

class editProfilePage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.editProfilePage()

    def editProfilePage(self):
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
            text="Change",
            fill="#000000",
            font=("Helvetica", 32 * -1)
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

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.origin.profilePage(),
            relief="flat"
        )
        self.button_8.place(
            x=916.0,
            y=639.0,
            width=147.0,
            height=26.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            172.0,
            479.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            362.0,
            650.0,
            anchor="nw",
            text="Warning",
            fill="#FF0101",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            3499.0,
            446.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            362.0,
            355.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            401.0,
            anchor="nw",
            text="Birthdate",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            453.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            499.0,
            anchor="nw",
            text="City",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            549.0,
            anchor="nw",
            text="Country",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            777.0,
            549.0,
            anchor="nw",
            text="Postal Code",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            164.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            309.0,
            anchor="nw",
            text="Full Name",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            212.0,
            anchor="nw",
            text="New Password",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            362.0,
            260.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            788.0,
            228.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_1.place(
            x=571.0,
            y=206.0,
            width=434.0,
            height=42.0
        )

        self.canvas.create_text(
            362.0,
            595.0,
            anchor="nw",
            text="Old Password",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            788.0,
            612.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_2.place(
            x=571.0,
            y=590.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            663.0,
            564.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_3.place(
            x=571.0,
            y=542.0,
            width=184.0,
            height=42.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            957.0,
            563.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_4.place(
            x=909.0,
            y=541.0,
            width=96.0,
            height=42.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            788.0,
            516.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_5.place(
            x=571.0,
            y=494.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            788.0,
            468.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_6.place(
            x=571.0,
            y=446.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            788.0,
            372.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_7.place(
            x=571.0,
            y=350.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            788.0,
            420.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_8.place(
            x=571.0,
            y=398.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            788.0,
            324.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_9.place(
            x=571.0,
            y=302.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            788.0,
            180.0,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_10.place(
            x=571.0,
            y=158.0,
            width=434.0,
            height=42.0
        )

        self.entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            788.0,
            276.0,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_11.place(
            x=571.0,
            y=254.0,
            width=434.0,
            height=42.0
        )

    #window.resizable(False, False)
    def startPage(self):
        self.mainloop()
