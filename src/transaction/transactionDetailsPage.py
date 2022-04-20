

import tkinter as tk
from pathlib import Path
from tkinter import *
from datetime import datetime, timezone


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/transaction details page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class transactionDetailsPage(tk.Frame):
    def __init__(self, master, pageManager, transaction):
        super().__init__(master)
        self.transaction = transaction
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

        if(self.origin.user.role == 'Member'):
            self.hoveredTat = PhotoImage(
            file=relative_to_assets("hoveredTat.png")) 
            self.tatImage = PhotoImage(
                file=relative_to_assets("tatButton.png")) 
            self.tatButton = Button(
                image =self.tatImage,
                borderwidth=0,
                highlightthickness=0,
                bg = "white",
                command=lambda: self._on_click_tat(),
                relief="flat"
            ) 
            self.tatButton.place(
                x=682.0,
                y=24.0,
                width=117.0,
                height=21.0
            )
            self.tatButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredTat))
            self.tatButton.bind("<Leave>", lambda e: e.widget.config(image = self.tatImage))
            
            
            self.hoveredCalendar = PhotoImage(
                file=relative_to_assets("hoveredCalendar.png")) 
            self.calendarImage = PhotoImage(
                file=relative_to_assets("calendarButton.png")) 
            self.calendarButton = Button(
                image =self.calendarImage,
                borderwidth=0,
                highlightthickness=0,
                bg = "white",
                command=lambda: self._on_click_calendar(),
                relief="flat"
            ) 
            self.calendarButton.place(
                x=858.0,
                y=24.0,
                width=68.0,
                height=22.0
            )
            self.calendarButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredCalendar))
            self.calendarButton.bind("<Leave>", lambda e: e.widget.config(image = self.calendarImage))

            self.hoveredHome = PhotoImage(
                file=relative_to_assets("hoveredHome.png"))
            self.homeImage = PhotoImage(
                file=relative_to_assets("homeButton.png")) 
            self.homeButton = Button(
                image =self.homeImage,
                borderwidth=0,
                highlightthickness=0,
                bg = "white",
                command=lambda: self._on_click_home(),
                relief="flat"
            ) 
            
            self.homeButton.place(
                x=559.0,
                y=24.0,
                width=47.0,
                height=22.0
            )
            self.homeButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredHome))
            self.homeButton.bind("<Leave>", lambda e: e.widget.config(image = self.homeImage))
        elif(self.origin.user.role == 'Guest'):
            self.hoveredHome = PhotoImage(
                file= relative_to_assets("hoveredHome.png"))
            self.homeImage = PhotoImage(
                file=relative_to_assets("homeButton.png"))
            self.homeButton = Button(
                image=self.homeImage,
                borderwidth=0,
                highlightthickness=0,
                bg="white",
                command=lambda: self._on_click_home(),
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

            self.image_image_1 = PhotoImage(
                file=relative_to_assets("image_1.png"))
            self.image_1 = self.canvas.create_image(
                538.0,
                443.0,
                image=self.image_image_1
            )
            
            self.homeButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredHome))
            self.homeButton.bind("<Leave>", lambda e: e.widget.config(image = self.homeImage))

            self.hoveredPricing = PhotoImage(
            file=relative_to_assets("hoveredPricing.png"))
            self.pricingImage = PhotoImage(
            file=relative_to_assets("pricingButton.png"))
            self.pricingButton = Button(
                image=self.pricingImage,
                borderwidth=0,
                highlightthickness=0,
                bg="white",
                command=lambda:self._on_click_pricing(),
                relief="flat"
            )
            self.pricingButton.place(
                x=803.0,
                y=24.0,
                width=54.0,
                height=21.0
            )
            self.pricingButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredPricing))
            self.pricingButton.bind("<Leave>", lambda e: e.widget.config(image = self.pricingImage))
        elif(self.origin.user.role == 'Admin'):
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
                x=879.0,
                y=28.0,
                width=47.0,
                height=22.0
            )
            self.homeButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredHome))
            self.homeButton.bind("<Leave>", lambda e: e.widget.config(image = self.homeImage))


        self.profileImage = PhotoImage(
            file=relative_to_assets("profileButton.png")) 
        self.profileButton = Button(
            image =self.profileImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_profile(),
            relief="flat"
        ) 
        self.profileButton.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
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
            text= self.transaction.cardNumber,
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            276.0,
            anchor="ne",
            text=self.transaction.bank,
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            381.0,
            anchor="ne",
            text= self.transaction.timeStamp.replace(tzinfo=timezone.utc).astimezone(tz=None),
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            490.0,
            anchor="ne",
            text= self.transaction.deadline.replace(tzinfo=timezone.utc).astimezone(tz=None),
            fill="#000000",
            font=("Helvetica", 15 * -1),
            width=485,
            justify="right"
        )

        self.canvas.create_text(
            676.0,
            436.0,
            anchor="ne",
            text='Rp{:0,.2f}'.format(self.transaction.price),
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

        self.backImage = PhotoImage(
            file=relative_to_assets("backButton.png"))
        self.backButton = Button(
            image=self.backImage,
            borderwidth=0,
            highlightthickness=0,
            bg = "#10429A",
            command=lambda: self._on_click_back(),
            relief="flat"
        )
        self.backButton.place(
            x=57.0,
            y=137.0,
            width=28.0,
            height=36.0
        )

    def startPage(self):
        self.mainloop()

    def _on_click_back(self):
        self.origin.myTransaction()

    def _on_click_pricing(self):
        self.origin.productPage()
    
    def _on_click_calendar(self):
        self.origin.calendarPage()

    def _on_click_home(self):
        self.origin.homePage()
    
    def _on_click_tat(self):
        self.origin.tipsAndTricksPage()
    
    def _on_click_profile(self):
        self.origin.profilePage()
