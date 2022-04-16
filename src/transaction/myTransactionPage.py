

import tkinter as tk
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
        
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png")) 
        self.button_1 = Button(
            image =self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg = "white",
            command=lambda: print("button_1 clicked"),
            relief="flat"
        ) 
        self.button_1.place(
            x=682.0,
            y=24.0,
            width=117.0,
            height=21.0
        )
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png")) 
        self.button_2 = Button(
            image =self.button_image_2,
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
            image =self.button_image_3,
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
        
        
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png")) 
        self.button_5 = Button(
            image =self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg = "white",
            command=lambda: print("button_5 clicked"),
            relief="flat"
        ) 
        self.button_5.place(
            x=559.0,
            y=24.0,
            width=47.0,
            height=22.0
        )
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png")) 
        self.image_1 = self.canvas.create_image(
            203.0,
            376.0,
            image =self.image_image_1
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
        
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png")) 
        self.button_6 = Button(
            image =self.button_image_6,
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
            image =self.button_image_7,
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
        
        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png")) 
        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))

        for i in range(20):
            self.newCanvas = Canvas(self.frame, 
                width = 635, 
                height=64,
                bd = 0,
                bg = "white",
                highlightthickness = 0,
                relief = "ridge"                
            )

            self.newCanvas.create_image(0, 0, image = self.image_image_4, anchor="nw")

            self.button_8 = Button(
                self.frame,
                image =self.button_image_8,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_8 clicked"),
                relief="flat"
            ) 


            self.newCanvas.create_text(
                165.0,
                24.0,
                anchor="nw",
                text="123456789101234",
                fill="#000000",
                font=("Helvetica", 15 * -1)
            )

            self.newCanvas.create_text(
                27.0,
                24.0,
                anchor="nw",
                text="2021-02-11",
                fill="#000000",
                font=("Helvetica", 15 * -1)
            )

            self.newCanvas.create_window(537.0, 24.0, window = self.button_8, anchor = "nw")
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

    


    