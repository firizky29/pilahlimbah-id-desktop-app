import transaction.orderPage as order
import transaction.productPage as product
import transaction.myTransactionPage as mytransaction
from tkinter import Tk


class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1080x700")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Enter>", self._on_hover)
        self.window.bind_class("Button", "<Leave>", self._leave_hover)
        # inisialisasi dengan page login/register, tapi sementara pake page product dulu
        self.page = mytransaction.myTransactionPage(master = self.window, pageManager = self)
    
    def run(self):
        self.page.startPage()

    def setUser(self, user):
        self.user = user

    def orderPage(self):
        self.page = order.orderPage(master = self.window, pageManager = self)
        self.page.startPage()

    def productPage(self):
        self.page = product.productPage(master = self.window, pageManager = self)
        self.page.startPage()

    def _on_hover(self, event):
        self.window.config(cursor = "hand2")
    
    def _leave_hover(self, event):
        self.window.config(cursor="")

        