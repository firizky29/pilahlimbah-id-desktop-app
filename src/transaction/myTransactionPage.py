

import tkinter as tk
from . import transaction
from pathlib import Path
from tkinter import *



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/my transaction page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class myTransactionPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.myTransactionPage()

    def myTransactionPage(self):
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
        self.createScrollableCanvas()

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
                command=lambda: print("tatButton clicked"),
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
                command=lambda: print("homeButton clicked"),
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
        elif(self.origin.user.role == 'Member'):
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
                command=self._on_click_pricing,
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
            command=lambda: print("profileButton clicked"),
            relief="flat"
        ) 
        self.profileButton.place(
            x=990.0,
            y=18.0,
            width=42.0,
            height=41.0
        )

        self.canvas.create_text(
            56.0,
            128.0,
            anchor="nw",
            text="Transactions.",
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
        
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png")) 
        self.image_2 = self.canvas.create_image(
            202.0,
            459.0,
            image =self.image_image_2
        )
        
        
        self.hoveredMyTransaction = PhotoImage(
            file=relative_to_assets("hoveredMyTransaction.png")) 
        self.myTransactionImage = PhotoImage(
            file=relative_to_assets("myTransactionButton.png")) 
        self.myTransactionButton = Button(
            image =self.myTransactionImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("myTransactionButton clicked"),
            relief="flat"
        ) 
        self.myTransactionButton.place(
            x=591.0,
            y=94.0,
            width=198.0,
            height=42.0
        )

        self.hoveredMyProfile = PhotoImage(
            file=relative_to_assets("hoveredMyProfile.png")) 
        self.myProfileImage = PhotoImage(
            file=relative_to_assets("myProfileButton.png")) 
        self.myProfileButton = Button(
            image =self.myProfileImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("myProfileButton clicked"),
            relief="flat"
        ) 
        self.myProfileButton.place(
            x=384.0,
            y=94.0,
            width=198.0,
            height=42.0
        )
        self.myProfileButton.bind("<Enter>", self._on_hover_transaction)
        self.myProfileButton.bind("<Leave>", self._leave_hover_transaction)

        
        
        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png")) 
        self.image_3 = self.canvas.create_image(
            715.0,
            203.0,
            image =self.image_image_3
        )

    


    def startPage(self):
        self.mainloop()

    # helper
    def createScrollableCanvas(self):
        self.scrollcanvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 506,
            width = 664,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.scrollcanvas.place(x = 392.0, y = 168.0)

        self.scroll_y = Scrollbar(self.canvas, orient="vertical", command=self.scrollcanvas.yview)
        self.scroll_y.place(x = 1046.0, y = 168.0, height = 506)

        self.frame = Frame(self.scrollcanvas, bg = "white")
        
        self.seeDetailsImage = PhotoImage(
            file=relative_to_assets("seeDetailsButton.png")) 
        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))

        myTransactions = self.origin.mydb.cursor(buffered = True)
        transaction_info = "account_number, cast(order_date as date)"
        transaction_details = "branch_name, order_date, ol.amount, deadline_date"
        tables = "orderlist as ol inner join account as ac on ol.account_id = ac.account_id natural inner join bank"
        requirement = f"user_id = {self.origin.user.userId}"
        addition = "order by order_date desc"
        myTransactions.execute("select " + transaction_info + " , " + transaction_details + " from " + tables + " where " + requirement + " "+ addition)
        sz = myTransactions.rowcount
        for i, order in enumerate(myTransactions):
            self.newCanvas = Canvas(self.frame, 
                width = 635, 
                height=64,
                bd = 0,
                bg = "white",
                highlightthickness = 0,
                relief = "ridge"                
            )
            cardNumber = order[0]
            order_date = order[1]
            cardNumber = cardNumber[:4]+"-"+cardNumber[4:8] + "-" + cardNumber[8:12] + "-" + cardNumber[12:16]
            self.newCanvas.create_image(0, 0, image = self.image_image_4, anchor="nw")

            order_details = {
                "card number" : cardNumber,
                "bank" : order[2],
                "timestamp" : order[3],
                "price" : order[4],
                "deadline" : order[5]
            }
            self.seeDetailsButton = Button(
                self.frame,
                image =self.seeDetailsImage,
                borderwidth=0,
                highlightthickness=0,
                command= lambda: self._on_click_see_details(transaction.transaction(order_details)),
                relief="flat"
            ) 


            self.newCanvas.create_text(
                165.0,
                24.0,
                anchor="nw",
                text=cardNumber,
                fill="#000000",
                font=("Helvetica", 15 * -1)
            )

            self.newCanvas.create_text(
                27.0,
                24.0,
                anchor="nw",
                text=order_date,
                fill="#000000",
                font=("Helvetica", 15 * -1)
            )

            self.newCanvas.create_window(537.0, 24.0, window = self.seeDetailsButton, anchor = "nw")
            self.newCanvas.grid(row = i, column=0, padx=10, pady=10)


        self.scrollcanvas.create_window(0, 0, 
            anchor='nw', 
            window=self.frame
        )
        
        self.scrollcanvas.update_idletasks()
        self.scrollcanvas.configure(scrollregion=self.scrollcanvas.bbox('all'), 
                        yscrollcommand=self.scroll_y.set)                  

        self.frame.bind('<Enter>', self._bound_to_mousewheel)
        self.frame.bind('<Leave>', self._unbound_to_mousewheel)


    def _bound_to_mousewheel(self, event):
        self.scrollcanvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.scrollcanvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.scrollcanvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_hover_transaction(self, event):
        event.widget.config(image = self.hoveredMyProfile)
        self.myTransactionButton.config(image=self.hoveredMyTransaction)

    def _leave_hover_transaction(self, event):
        event.widget.config(image = self.myProfileImage)
        self.myTransactionButton.config(image=self.myTransactionImage)

    def _on_click_see_details(self, transaction):
        self.origin.transactionDetails(transaction)

    def _on_click_pricing(self):
        self.origin.productPage()
    
    def _on_click_calendar(self):
        self.origin.calendarPage()


    


    