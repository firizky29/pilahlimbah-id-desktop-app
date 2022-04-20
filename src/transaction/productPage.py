"""
    File ini adalah file productPage.py
    File ini berfungsi untuk menampilkan product yang disediakan
"""

from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/product page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class productPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.productPage()

    def productPage(self):
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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            565.0,
            429.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            887.0,
            429.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            205.0,
            372.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            191.0,
            513.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            36.0,
            24.0,
            anchor="nw",
            text="PilahLimbah.id",
            fill="#000000",
            font=("Helvetica", 20 * -1, "bold")
        )

        self.canvas.create_text(
            442.0,
            227.0,
            anchor="nw",
            text="Starter",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            421.0,
            102.0,
            anchor="nw",
            text="Get Started Today!",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            421.0,
            143.0,
            anchor="nw",
            text="Let\'s make our earth a better world",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.pricingImage = PhotoImage(
            file=relative_to_assets("pricingButton.png"))
        self.pricingButton = Button(
            image=self.pricingImage,
            borderwidth=0,
            highlightthickness=0,
            bg = "white",
            command=lambda: print("pricingButton clicked"),
            relief="flat"
        )
        self.pricingButton.place(
            x=803.0,
            y=24.0,
            width=54.0,
            height=21.0
        )

        self.hoveredProfile = PhotoImage(
            file=relative_to_assets("hoveredProfile.png"))
        self.profileImage = PhotoImage(
            file=relative_to_assets("profileButton.png"))
        self.profileButton = Button(
            image=self.profileImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("profileButton clicked"),
            relief="flat"
        )
        self.profileButton.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
        )
        self.profileButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredProfile))
        self.profileButton.bind("<Leave>", lambda e: e.widget.config(image = self.profileImage))

        self.canvas.create_text(
            768.0,
            227.0,
            anchor="nw",
            text="Pro",
            fill="#F7F9FA",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            61.0,
            155.0,
            anchor="nw",
            text="Earth now.",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            61.0,
            121.0,
            anchor="nw",
            text="Save our",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_text(
            442.0,
            280.0,
            anchor="nw",
            text="Rp0.00/Month",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.canvas.create_text(
            442.0,
            330.0,
            anchor="nw",
            text="Features included are",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            484.0,
            366.0,
            anchor="nw",
            text="Eco-friendly content",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            484.0,
            418.0,
            anchor="nw",
            text="Manage profile",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            484.0,
            366.0,
            anchor="nw",
            text="Eco-friendly content",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            484.0,
            418.0,
            anchor="nw",
            text="Manage profile",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            816.0,
            369.0,
            anchor="nw",
            text="Eco-friendly content",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            817.0,
            418.0,
            anchor="nw",
            text="Manage profile",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            816.0,
            466.0,
            anchor="nw",
            text="Tips and tricks from expert",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            817.0,
            514.0,
            anchor="nw",
            text="Eco-daily manager",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            484.0,
            466.0,
            anchor="nw",
            text="Free forever!",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            330.0,
            anchor="nw",
            text="Features included are",
            fill="#FFFFFF",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            768.0,
            280.0,
            anchor="nw",
            text="Rp46.000.00/Month",
            fill="#F7F9FA",
            font=("Helvetica", 20 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            565.0,
            607.0,
            image=self.image_image_5
        )

        self.hoveredJoin = PhotoImage(
            file=relative_to_assets("hoveredJoin.png")
        )
        self.joinImage = PhotoImage(
            file=relative_to_assets("joinButton.png"))
        self.joinButton = Button(
            image=self.joinImage,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            command= self._on_click_join,
            relief="flat"
        )
        self.joinButton.place(
            x=789.0,
            y=590.0,
            width=198.0,
            height=42.0
        )
        self.joinButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredJoin))
        self.joinButton.bind("<Leave>", lambda e: e.widget.config(image = self.joinImage))

        self.canvas.create_rectangle(
            442.0,
            316.0,
            490.0,
            321.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            768.0,
            316.0,
            816.0,
            321.0,
            fill="#FFFFFF",
            outline="")

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            780.0,
            380.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            453.0,
            380.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            781.0,
            429.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            454.0,
            429.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            781.0,
            478.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            781.0,
            527.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            454.0,
            478.0,
            image=self.image_image_12
        )

        self.hoveredHome = PhotoImage(
            file= relative_to_assets("hoveredHome.png"))
        self.homeImage = PhotoImage(
            file=relative_to_assets("homeButton.png"))
        self.homeButton = Button(
            image=self.homeImage,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            command=lambda: print("homeButton clicked"),
            relief="flat"
        )
        self.homeButton.place(
            x=681.0,
            y=24.0,
            width=47.0,
            height=22.0
        )
        self.homeButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredHome))
        self.homeButton.bind("<Leave>", lambda e: e.widget.config(image = self.homeImage))

    def startPage(self):
        self.mainloop()

    def _on_click_join(self):
        self.origin.orderPage()
    
