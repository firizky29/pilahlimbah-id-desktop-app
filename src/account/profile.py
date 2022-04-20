import tkinter as tk
import tkinter.messagebox as msg
from pathlib import Path
from tkinter import *
from datetime import timezone
from . import user

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/profile page")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




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
                command=lambda: self._on_click_home(),
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
        

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_profile(),
            relief="flat"
        )
        self.button_2.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
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
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            56.0,
            94.0,
            anchor="nw",
            text="My",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            202.0,
            459.0,
            image=self.image_image_1
        )

        self.hoveredMyTransactions = PhotoImage(
            file=relative_to_assets("hoveredMyTransactions.png")) 
        self.myTransactionsImage = PhotoImage(
            file=relative_to_assets("myTransactions.png")) 
        self.myTransactionsButton = Button(
            image =self.myTransactionsImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_transaction(),
            relief="flat"
        ) 
        self.myTransactionsButton.place(
            x=591.0,
            y=94.0,
            width=198.0,
            height=42.0
        )
        self.myTransactionsButton.bind("<Enter>", self._on_hover_transaction)
        self.myTransactionsButton.bind("<Leave>", self._leave_hover_transaction)


        self.hoveredMyProfile = PhotoImage(
            file=relative_to_assets("hoveredMyProfile.png"))
        self.myProfileImage = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.myProfileButton = Button(
            image=self.myProfileImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_profile(),
            relief="flat"
        )
        self.myProfileButton.place(
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
            text=self.origin.user.gender,
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
            text=self.origin.user.address,
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
            text=self.origin.user.city,
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
            text=self.origin.user.country,
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
            text=self.origin.user.postalCode,
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
            text=self.origin.user.birthdate,
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

        roles = self.origin.user.role
        if(roles == 'Member'):
            roles = roles + " (until " + str(self.origin.user.deadline.replace(tzinfo=timezone.utc).astimezone(tz=None)) +")"
        self.canvas.create_text(
            619.0,
            335.0,
            anchor="nw",
            text= roles,
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


        self.button_image_5 = PhotoImage(
            file=relative_to_assets("logout.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_exit(),
            bg = 'white',
            relief="flat"
        )
        self.button_5.place(
            x=931.0,
            y=647.0,
            width=54.0,
            height=42.0
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
            text=self.origin.user.username,
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
            text=self.origin.user.email,
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
            text=self.origin.user.fullname,
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


    def _on_click_exit(self):
        MsgBox = msg.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            self.origin.user = None
            self.origin.loginPage()

    def _on_hover_transaction(self, event):
        event.widget.config(image = self.hoveredMyTransactions)
        self.myProfileButton.config(image=self.hoveredMyProfile)

    def _leave_hover_transaction(self, event):
        event.widget.config(image = self.myTransactionsImage)
        self.myProfileButton.config(image=self.myProfileImage)

    def _on_click_transaction(self):
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

            
