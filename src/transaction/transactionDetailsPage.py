

import tkinter as tk
from pathlib import Path
from tkinter import *
from turtle import bgcolor


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/transaction details page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class transactionDetailsPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.transactionDetailsPage()

    def transactionDetailsPage(self):
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
            highlightthickness=0,
            bg = "white",
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
            bg = "white",
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
            bg = "white",
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
            711.0,
            83.0,
            1045.0,
            679.0,
            fill="#F7F9FA",
            outline="")

        self.canvas.create_text(
            731.0,
            133.0,
            anchor="nw",
            text="Details",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            731.0,
            99.0,
            anchor="nw",
            text="Transaction",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            877.0,
            503.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            370.0,
            155.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            359.0,
            382.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            89.0,
            143.0,
            anchor="nw",
            text="Overview",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.canvas.create_text(
            52.0,
            222.0,
            anchor="nw",
            text="Card Number",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.canvas.create_text(
            676.0,
            221.0,
            anchor="ne",
            text="123456789101234",
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            276.0,
            anchor="ne",
            text="BCA Corporate",
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            381.0,
            anchor="ne",
            text="2021-02-11 00:00:00 UTC+8",
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            490.0,
            anchor="ne",
            text="2021-02-11 00:00:00 UTC+8",
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            436.0,
            anchor="ne",
            text="Rp46.000.00",
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            332.0,
            anchor="ne",
            text="Success",
            fill="#298F55",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            52.0,
            276.0,
            anchor="nw",
            text="Bank",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.canvas.create_text(
            52.0,
            328.0,
            anchor="nw",
            text="Status",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.canvas.create_text(
            52.0,
            382.0,
            anchor="nw",
            text="Timestamp",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.canvas.create_text(
            52.0,
            436.0,
            anchor="nw",
            text="Amount",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.canvas.create_text(
            52.0,
            490.0,
            anchor="nw",
            text="Active Deadline",
            fill="#000000",
            font=("Helvetica", 15 * -1, "bold")
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            605.0,
            342.0,
            image=self.image_image_4
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            bg = "#10429A",
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=57.0,
            y=137.0,
            width=28.0,
            height=36.0
        )

    def startPage(self):
        self.mainloop()