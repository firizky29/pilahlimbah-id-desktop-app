

import tkinter as tk
import hashlib
from . import transaction
from pathlib import Path
from tkinter import *
from datetime import datetime, timezone


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

        self.cardNumber = tk.StringVar()
        self.securityCode = tk.StringVar()
        self.address = tk.StringVar()
        self.city = tk.StringVar()
        self.country = tk.StringVar()
        self.postalCode = tk.StringVar()

        self.cardNumber.trace("w", self._cardNumber_trace)
        self.securityCode.trace("w", self._securityCode_trace)
        self.postalCode.trace("w", self._postalCode_trace)
        

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
            83.0,
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

        
        self.hoveredPay = PhotoImage(
            file= relative_to_assets("hoveredPay.png"))
        self.payImage = PhotoImage(
            file=relative_to_assets("payButton.png"))
        self.payButton = Button(
            image=self.payImage,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            command=self._on_submit_pay,
            relief="flat"
        )
        self.payButton.place(
            x=812.0,
            y=629.0,
            width=198.0,
            height=42.0
        )
        self.payButton.bind("<Enter>", lambda e: e.widget.config(image = self.hoveredPay))
        self.payButton.bind("<Leave>", lambda e: e.widget.config(image = self.payImage))
        

        

        self.largeEntryImage = PhotoImage(
            file=relative_to_assets("largeEntry.png"))
        self.smallEntryImage = PhotoImage(
            file=relative_to_assets("smallEntry.png"))
        self.midEntryImage = PhotoImage(
            file=relative_to_assets("midEntry.png"))
        self.entry_bg_1 = self.canvas.create_image(
            569.0,
            261.0,
            image=self.midEntryImage
        )
        self.cardEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.cardNumber
        )
        self.cardEntry.place(
            x=360.0,
            y=229.0 + 28.0,
            width=418.0,
            height=36.0
        )

        self.entry_bg_7 = self.canvas.create_image(
            908.5,
            261.0,
            image=self.smallEntryImage
        )
        self.securityCodeEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.securityCode,
            show="*"
        )
        self.securityCodeEntry.place(
            x=830.0,
            y=229.0 + 28.0,
            width=157.0,
            height=36.0
        )

        self.entry_bg_2 = self.canvas.create_image(
            676.0,
            341.0,
            image=self.largeEntryImage
        )
        self.bank = Label(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
        )
        self.bank.place(
            x=360.0,
            y=309.0 + 28.0,
            anchor = "nw"
        )

        self.entry_bg_3 = self.canvas.create_image(
            676.0,
            421.0,
            image=self.largeEntryImage
        )
        self.addressEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.address
        )
        self.addressEntry.place(
            x=360.0,
            y=389.0 + 28.0,
            width=632.0,
            height=36.0
        )



        self.entry_bg_4 = self.canvas.create_image(
            676.0,
            501.0,
            image=self.largeEntryImage
        )
        self.cityEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.city
        )
        self.cityEntry.place(
            x=360.0,
            y=469.0 + 28.0,
            width=632.0,
            height=36.0
        )

        self.entry_bg_5 = self.canvas.create_image(
            569.0,
            581.0,
            image=self.midEntryImage
        )
        self.countryEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.country
        )
        self.countryEntry.place(
            x=360.0,
            y=549.0 + 28.0,
            width=418.0,
            height=36.0
        )

        self.entry_bg_6 = self.canvas.create_image(
            908.5,
            581.0,
            image=self.smallEntryImage
        )
        self.postalCodeEntry = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.postalCode
        )
        self.postalCodeEntry.place(
            x=830.0,
            y=549.0 + 28.0,
            width=157.0,
            height=36.0
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
        self.canvas.create_text(
            354.0,
            394.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Helvetica", 16 * -1)
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
            829.0,
            554.0,
            anchor="nw",
            text="Postal Code",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )
        self.canvas.create_text(
            829.0,
            234.0,
            anchor="nw",
            text="Security Code",
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

        self.warning = Label(
            self.canvas,
            text="Warning",
            bg = "white",
            fg="white",
            font=("Helvetica", 16 * -1)
        )

        self.warning.place(
            x = 350.0,
            y = 629.0,
            anchor="nw"
        )

        self.canvas.bind_class("Entry","<Return>", lambda e: self._on_submit_pay())

        

    def startPage(self):
        self.mainloop()

    def _on_click_pricing(self):
        self.origin.productPage()

    def _on_submit_pay(self):
        self.warning["fg"] = "white"
        raw_transaction = {
            "user" : self.origin.user,
            "card number" : self.cardNumber.get(),
            "bank" : self.bank['text'],
            "security code" : self.securityCode.get(),
            "address" : self.address.get(),
            "city"  : self.city.get(),
            "country" : self.country.get(),
            "postal code" : self.postalCode.get(),
            "timestamp" : datetime.now(timezone.utc),
            "active period" : 30,
            "price" : 46000
        }
        temp = transaction.transaction(raw_transaction = raw_transaction, pageManager = self.origin)
        if(not(temp.status)):
            self.warning["text"] = temp.getWarning()
            self.warning["fg"] = "#FF0101"
        else:
            self.origin.successPage(temp)


    def _cardNumber_trace(self, *args):
        value = self.cardNumber.get()
        idx = self.cardEntry.index(INSERT)
        if len(value) > 19: 
            self.cardNumber.set(value[:idx-1]+value[idx:19])
            self.cardEntry.icursor(idx-1)
        if len(value) == 16:
            credit_bank = self.origin.mydb.cursor(buffered=True)
            credit_bank.execute(f"select branch_name from account natural inner join bank where account_number = '{value}'")
            if(credit_bank.rowcount!=0):
                self.bank["text"] = credit_bank.fetchone()[0]
            self.cardNumber.set(value[:4]+"-"+value[4:8] + "-" + value[8:12] + "-" + value[12:16])
        if len(value) == 18:
            self.cardNumber.set(value.replace("-", ""))
            self.bank["text"] = ""

    def _securityCode_trace(self, *args):
        value = self.securityCode.get()
        if len(value) > 5: self.securityCode.set(value[:5])
    
    def _postalCode_trace(self, *args):
        value = self.postalCode.get()
        if len(value) > 5: self.postalCode.set(value[:5])

        

