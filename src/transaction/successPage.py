

import tkinter as tk
from pathlib import Path
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/success page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class successPage(tk.Frame):
    def __init__(self, master, pageManager, transaction):
        super().__init__(master)
        self.transaction = transaction
        self.master = master
        self.origin = pageManager
        self.pack()
        self.successPage()

    def successPage(self):
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

        self.hoveredProfile = PhotoImage(
            file=relative_to_assets("hoveredProfile.png"))
        self.profileImage = PhotoImage(
            file=relative_to_assets("profileButton.png"))
        self.profileButton = Button(
            image=self.profileImage,
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
        self.profileButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredProfile))
        self.profileButton.bind("<Leave>", lambda e: e.widget.config(image = self.profileImage))

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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            540.0,
            319.0,
            image=self.image_image_1
        )

        self.hoveredGetStarted = PhotoImage(
            file=relative_to_assets("hoveredGetStarted.png"))
        self.getStartedImage = PhotoImage(
            file=relative_to_assets("getStartedButton.png"))
        self.getStartedButton = Button(
            image=self.getStartedImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_home(),
            relief="flat"
        )
        self.getStartedButton.place(
            x=441.0,
            y=514.0,
            width=198.0,
            height=42.0
        )
        self.getStartedButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredGetStarted))
        self.getStartedButton.bind("<Leave>", lambda e: e.widget.config(image = self.getStartedImage))

        self.hoveredSeeDetails = PhotoImage(
            file=relative_to_assets("hoveredSeeDetails.png"))
        self.seeDetailsImage = PhotoImage(
            file=relative_to_assets("seeDetailsButton.png"))
        self.seeDetailsButton = Button(
            image=self.seeDetailsImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_seeDetails(),
            relief="flat"
        )
        self.seeDetailsButton.place(
            x=441.0,
            y=572.0,
            width=198.0,
            height=42.0
        )
        self.seeDetailsButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredSeeDetails))
        self.seeDetailsButton.bind("<Leave>", lambda e: e.widget.config(image = self.seeDetailsImage))

        self.canvas.create_text(
            461.0,
            478.0,
            anchor="nw",
            text="Transaction",
            fill="#000000",
            font=("Helvetica", 15 * -1)
        )

        self.canvas.create_text(
            545.0,
            478.0,
            anchor="nw",
            text="successful!",
            fill="#298F55",
            font=("Helvetica", 15 * -1)
        )

    def startPage(self):
        self.mainloop()

    def _on_click_seeDetails(self):
        self.origin.transactionDetails(self.transaction)

    def _on_click_calendar(self):
        self.origin.calendarPage()

    def _on_click_home(self):
        self.origin.homePage()
    
    def _on_click_tat(self):
        self.origin.tipsAndTricksPage()
    
    def _on_click_profile(self):
        self.origin.profilePage()
