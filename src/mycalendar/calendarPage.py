
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime

from tkcalendar import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../img/calendar page")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class calendarPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.canvas = Canvas()
        self.calendar = Calendar()
        self.display_date = ""
        self.display_cnt_task = ""

        # to do list
        # task 1
        self.task1_done = ""
        self.task1_not_done = ""
        self.task1_name = ""
        self.task1_desc = ""

        # task 2
        self.task2_done = ""
        self.task2_not_done = ""
        self.task2_name = ""
        self.task2_desc = ""

        # task 3
        self.task3_done = ""
        self.task3_not_done = ""
        self.task3_name = ""
        self.task3_desc = ""

        self.calendarPage()    

    # mark task as done
    def mark_done_task1(self):
        set_done = self.origin.mydb.cursor()
        set_done.execute(f"INSERT INTO activity values('{self.calendar.get_date()}',1,'{self.origin.user.userId}','{datetime.now()}')")
        self.canvas.itemconfig(self.task1_done, text = "Done");
        self.canvas.itemconfig(self.task1_not_done, text = "")
        self.origin.mydb.commit()

    def mark_done_task2(self):
        set_done = self.origin.mydb.cursor()
        set_done.execute(f"INSERT INTO activity values('{self.calendar.get_date()}',2,'{self.origin.user.userId}','{datetime.now()}')")
        self.canvas.itemconfig(self.task2_done, text = "Done");
        self.canvas.itemconfig(self.task2_not_done, text = "")
        self.origin.mydb.commit()
    
    def mark_done_task3(self):
        set_done = self.origin.mydb.cursor()
        set_done.execute(f"INSERT INTO activity values('{self.calendar.get_date()}',3,'{self.origin.user.userId}','{datetime.now()}')")
        self.canvas.itemconfig(self.task3_done, text = "Done");
        self.canvas.itemconfig(self.task3_not_done, text = "")
        self.origin.mydb.commit()

    def open_to_do(self): 
        # display date which is selected by button
        self.canvas.itemconfig(self.display_date, text=self.calendar.get_date())
        
        # create new cursor
        mytask = self.origin.mydb.cursor(buffered=True)
        mytask.execute(f"SELECT * FROM task WHERE task_date='{self.calendar.get_date()}'")
        
        # count task
        cnt = 0

        # initialize array of task
        list_task_name = ["" for i in range(3)]
        list_task_desc = ["" for i in range(3)]
        list_task_id = [0 for i in range(3)]

        # store database in array
        for i in mytask:
            list_task_name[cnt] = str(i[2])
            list_task_desc[cnt] = str(i[3])
            list_task_id[cnt] = str(i[1])
            cnt += 1;

        # display count task
        self.canvas.itemconfig(self.display_cnt_task, text=str(cnt))

        # clear display because there're no task
        self.canvas.itemconfig(self.task1_desc, text="-")
        self.canvas.itemconfig(self.task1_name, text="-")  
        self.canvas.itemconfig(self.task1_done, text="")
        self.canvas.itemconfig(self.task1_not_done, text="")

        self.canvas.itemconfig(self.task2_desc, text="-")
        self.canvas.itemconfig(self.task2_name, text="-")  
        self.canvas.itemconfig(self.task2_done, text="")
        self.canvas.itemconfig(self.task2_not_done, text="")

        self.canvas.itemconfig(self.task3_desc, text="-")
        self.canvas.itemconfig(self.task3_name, text="-")  
        self.canvas.itemconfig(self.task3_done, text="")
        self.canvas.itemconfig(self.task3_not_done, text="")
        
        # there are more than 1 task that should be done
        if(cnt > 0): 
            
            # task 1
            if(list_task_name[0] != ""):
                activity1 = self.origin.mydb.cursor(buffered=True)
                activity1.execute(f"SELECT activity_date, task_id FROM activity WHERE task_id={list_task_id[0]} AND activity_date='{self.calendar.get_date()}' AND member_id = '{self.origin.user.userId}'")
                if activity1.rowcount == 0:
                    self.canvas.itemconfig(self.task1_not_done, text = "Not Done")
                else:
                    self.canvas.itemconfig(self.task1_done,text = "Done")
                self.canvas.itemconfig(self.task1_name, text = list_task_name[0])
                self.canvas.itemconfig(self.task1_desc, text = list_task_desc[0][:35]+'...')
            
            # task 2
            if(list_task_name[1] != ""):
                activity2 = self.origin.mydb.cursor(buffered=True)
                activity2.execute(f"SELECT activity_date, task_id FROM activity WHERE task_id={list_task_id[1]} AND activity_date='{self.calendar.get_date()}' AND member_id = '{self.origin.user.userId}'")
                if activity2.rowcount == 0:
                    self.canvas.itemconfig(self.task2_not_done, text = "Not Done")
                else:
                    self.canvas.itemconfig(self.task2_done,text = "Done") 
                self.canvas.itemconfig(self.task2_name, text = list_task_name[1])
                self.canvas.itemconfig(self.task2_desc, text = list_task_desc[1][:35]+'...')
            
            # task 3
            if(list_task_name[2] != ""):
                activity3 = self.origin.mydb.cursor(buffered=True)
                activity3.execute(f"SELECT activity_date, task_id FROM activity WHERE task_id={list_task_id[2]} AND activity_date='{self.calendar.get_date()}' AND member_id = '{self.origin.user.userId}'")
                if activity3.rowcount == 0:
                    self.canvas.itemconfig(self.task3_not_done, text = "Not Done")
                else:
                    self.canvas.itemconfig(self.task3_done,text = "Done")
                self.canvas.itemconfig(self.task3_name, text = list_task_name[2])
                self.canvas.itemconfig(self.task3_desc, text = list_task_desc[2][:35]+'...')

    def calendarPage(self):

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

        self.calendar = Calendar(self.canvas, setmode="day", date_pattern = 'yyyy-mm-dd')
        self.calendar.place(
            x = 415,
            y = 152
        )

        self.open_calendar = Button(self.calendar, text="open to do list",command=self.open_to_do) 
        self.open_calendar.pack(padx=15,pady=15)

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            536.0,
            527.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            120.0,
            39.0,
            image=self.image_image_2
        )

        # self.button_image_1 = PhotoImage(
        #     file=relative_to_assets("button_1.png"))
        # self.button_1 = Button(
        #     image=self.button_image_1,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_1 clicked"),
        #     relief="flat"
        #     , bg='white'
        # )
        # self.button_1.place(
        #     x=682.0,
        #     y=24.0,
        #     width=112.0,
        #     height=22.0
        # )

        # self.button_image_2 = PhotoImage(
        #     file=relative_to_assets("button_2.png"))
        # self.button_2 = Button(
        #     image=self.button_image_2,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_2 clicked"),
        #     relief="flat"
        #     , bg='white'
        # )
        # self.button_2.place(
        #     x=990.0,
        #     y=18.0,
        #     width=42.0,
        #     height=41.0
        # )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_calendar(),
            relief="flat"
            , bg='white'
        )
        self.button_3.place(
            x=858.0,
            y=24.0,
            width=68.0,
            height=22.0
        )

        # self.button_image_4 = PhotoImage(
        #     file=relative_to_assets("button_4.png"))
        # self.button_4 = Button(
        #     image=self.button_image_4,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_4 clicked"),
        #     relief="flat"
        #     , bg='white'
        # )
        # self.button_4.place(
        #     x=559.0,
        #     y=24.0,
        #     width=47.0,
        #     height=22.0
        # )

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

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            203.0,
            357.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            200.0,
            180.0,
            image=self.image_image_4
        )

        self.display_cnt_task = self.canvas.create_text(
            475.0,
            472.0,
            anchor="nw",
            text="0",
            fill="#585E62",
            font=("Helvetica", 40 * -1, "bold")
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            558.0,
            493.0,
            image=self.image_image_5
        )

        self.display_date = self.canvas.create_text(
            425.0,
            565.0,
            anchor="nw",
            text="select date",
            fill="#585E62",
            font=("Helvetica", 40 * -1, "bold"),
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            200.0,
            140.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            202.0,
            441.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            536.0,
            244.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            867.0,
            359.0,
            image=self.image_image_9
        )

        self.task1_name = self.canvas.create_text(
            768.0,
            163.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.task2_name = self.canvas.create_text(
            768.0,
            318.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.task3_name = self.canvas.create_text(
            768.0,
            482.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 16 * -1)
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            736.0,
            174.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            735.0,
            332.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            736.0,
            493.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = self.canvas.create_image(
            534.0,
            121.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = self.canvas.create_image(
            857.0,
            121.0,
            image=self.image_image_14
        )

        self.canvas.create_rectangle(
            424.0,
            152.0,
            644.0,
            365.0,
            fill="#E1E7EB",
            outline="")

        self.canvas.create_text(
            727.0,
            195.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            352.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.canvas.create_text(
            725.0,
            514.0,
            anchor="nw",
            text="Description:\n",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.task1_done = self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task1_not_done = self.canvas.create_text(
            926.0,
            163.0,
            anchor="nw",
            text="",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task2_done = self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task2_not_done = self.canvas.create_text(
            926.0,
            318.0,
            anchor="nw",
            text="",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task3_done = self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="",
            fill="#298F55",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task3_not_done = self.canvas.create_text(
            926.0,
            483.0,
            anchor="nw",
            text="",
            fill="#F5C855",
            font=("Helvetica", 16 * -1, "bold")
        )

        self.task1_desc = self.canvas.create_text(
            727.0,
            223.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.task2_desc = self.canvas.create_text(
            723.0,
            379.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.task3_desc = self.canvas.create_text(
            723.0,
            540.0,
            anchor="nw",
            text="-",
            fill="#000000",
            font=("Helvetica", 12 * -1)
        )

        self.image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.image_15 = self.canvas.create_image(
            529.0,
            446.0,
            image=self.image_image_15
        )

        self.image_image_16 = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.image_16 = self.canvas.create_image(
            529.0,
            544.0,
            image=self.image_image_16
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.mark_done_task1,
            relief="flat"
            , bg='white'
        )
        self.button_5.place(
            x=808.0,
            y=275.0,
            width=98.0,
            height=19.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.mark_done_task2,
            relief="flat"
            , bg='white'
        )
        self.button_6.place(
            x=808.0,
            y=441.0,
            width=98.0,
            height=19.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.mark_done_task3,
            relief="flat"
            , bg='white'
        )
        self.button_7.place(
            x=808.0,
            y=590.0,
            width=98.0,
            height=19.0
        )
        
    def startPage(self):
        self.mainloop()

    def _on_click_calendar(self):
        self.origin.calendarPage()

    def _on_click_home(self):
        self.origin.homePage()
    
    def _on_click_tat(self):
        self.origin.tipsAndTricksPage()
    
    def _on_click_profile(self):
        self.origin.profilePage()
