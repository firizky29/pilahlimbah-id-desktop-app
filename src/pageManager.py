import transaction.orderPage as order
import transaction.productPage as product
from tkinter import Tk


class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1080x700")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)

        # inisialisasi dengan page login/register, tapi sementara pake page product dulu
        self.page = product.productPage(master = self.window, pageManager = self)
    
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
        