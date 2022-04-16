

import tkinter as tk
from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/order page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class orderPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.orderPage()

    def orderPage(self):
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
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            bg = "white",
            highlightthickness=0,
            command= lambda: self.origin.productPage(),
            relief="flat"
        )
        self.button_1.place(
            x=803.0,
            y=24.0,
            width=54.0,
            height=21.0
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
            bg = "white",
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=681.0,
            y=24.0,
            width=47.0,
            height=22.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            538.0,
            443.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            676.0,
            261.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_1.place(
            x=360.0,
            y=229.0 + 28.0,
            width=632.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            676.0,
            341.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_2.place(
            x=360.0,
            y=309.0  + 28.0,
            width=632.0,
            height=36.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            187.0,
            489.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            533.0,
            127.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            76.0,
            72.0,
            anchor="nw",
            text="Pro",
            fill="#F7F9FA",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            76.0,
            125.0,
            anchor="nw",
            text="Rp46.000.00/Month",
            fill="#F7F9FA",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_rectangle(
            76.0,
            161.0,
            124.0,
            166.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            364.0,
            90.0,
            anchor="nw",
            text="Eco-friendly content",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            364.0,
            138.0,
            anchor="nw",
            text="Manage profile",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            758.0,
            90.0,
            anchor="nw",
            text="Tips and tricks from expert",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            759.0,
            138.0,
            anchor="nw",
            text="Eco-daily manager",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            329.0,
            102.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            329.0,
            151.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            723.0,
            102.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            723.0,
            151.0,
            image=self.image_image_7
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
            x=812.0,
            y=629.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            354.0,
            234.0,
            anchor="nw",
            text="Card Number",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            354.0,
            314.0,
            anchor="nw",
            text="Bank",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            676.0,
            421.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_3.place(
            x=360.0,
            y=389.0 + 28.0,
            width=632.0,
            height=36.0
        )

        self.canvas.create_text(
            354.0,
            394.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            676.0,
            501.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_4.place(
            x=360.0,
            y=469.0  + 28.0,
            width=632.0,
            height=36.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            569.0,
            581.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_5.place(
            x=360.0,
            y=549.0  + 28.0,
            width=418.0,
            height=36.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            908.5,
            581.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0
        )
        self.entry_6.place(
            x=830.0,
            y=549.0 + 28.0,
            width=157.0,
            height=36.0
        )

        self.canvas.create_text(
            354.0,
            474.0,
            anchor="nw",
            text="City",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            354.0,
            554.0,
            anchor="nw",
            text="Country",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            350.0,
            629.0,
            anchor="nw",
            text="Warning",
            fill="#FF0101",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            829.0,
            554.0,
            anchor="nw",
            text="Postal Code",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            76.0,
            263.0,
            anchor="nw",
            text="Details.",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            76.0,
            223.0,
            anchor="nw",
            text="Payment",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

    def startPage(self):
        self.mainloop()

# def startPage():
#     window = Tk()
#     window.geometry("1080x700")
#     window.configure(bg = "#FFFFFF")
#     window.resizable(False, False)
#     page = orderPage(master = window)
#     page.mainloop()