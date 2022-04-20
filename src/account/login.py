import tkinter as tk
from pathlib import Path
from tkinter import *
from . import user

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/login page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





class loginPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.loginPage()

    def loginPage(self):
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

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            552.0,
            400.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            196.0,
            422.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.origin.registerPage(),
            relief="flat"
        )
        self.button_1.place(
            x=582.0,
            y=533.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            540.0,
            495.0,
            anchor="nw",
            text="Is This Your First Time Here?",
            fill="#000000",
            font=("Helvetica", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            681.0,
            215.0,
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
            x=509.0,
            y=183.0,
            width=344.0,
            height=62.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            681.0,
            337.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F2EFF9",
            highlightthickness=0,
            font=("Calibri", 20 * -1),
            textvariable=self.password,
            show = "*"
        )
        self.entry_2.place(
            x=509.0,
            y=305.0,
            width=344.0,
            height=62.0
        )

        self.canvas.create_rectangle(
            76.0,
            161.0,
            124.0,
            166.0,
            fill="#FFFFFF",
            outline="")

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_submit_login(),
            relief="flat"
        )
        self.button_2.place(
            x=582.0,
            y=410.0,
            width=198.0,
            height=42.0
        )

        self.canvas.create_text(
            85.0,
            162.0,
            anchor="nw",
            text="Page.",
            fill="#000000",
            font=("Helvetica", 32 * -1, "bold")
        )

        self.canvas.create_text(
            85.0,
            119.0,
            anchor="nw",
            text="Login",
            fill="#000000",
            font=("Helvetica", 32 * -1)
        )

        self.canvas.create_text(
            645.0,
            153.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.canvas.create_text(
            645.0,
            272.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.warning = Label(
            self.canvas,
            text="Warning",
            bg = "white",
            fg="white",
            font=("Helvetica", 16 * -1)
        )

        self.warning.place(
            x = 499.0,
            y = 380.0,
            anchor="nw",
        )

        self.canvas.bind_class("Entry","<Return>", lambda e: self._on_submit_login())


    def startPage(self):
        self.mainloop()

    def _on_submit_login(self):
        self.warning["fg"] = "white"
        self.origin.user = user.user([self.username.get(), self.password.get()], self.origin)
        if(not self.origin.user.status):
            self.warning["text"] = self.origin.user.warning
            self.warning["fg"] = "#FF0101"
        else:
            if(self.origin.user.role == 'Admin'):
                self.origin.homePage()
            else:
                self.origin.homePage()

    def _on_click_create_account(self):
        self.origin.registerPage()

