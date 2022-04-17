import transaction.orderPage as order
import transaction.productPage as product
import transaction.myTransactionPage as mytransaction
import transaction.successPage as success
import transaction.transactionDetailsPage as transactionDetails
from tkinter import Tk


class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1080x700")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Enter>", self.__onHover__)
        self.window.bind_class("Button", "<Button-1>", self.__onClick__)
        # inisialisasi dengan page login/register, tapi sementara pake page product dulu
        self.page = transactionDetails.transactionDetailsPage(master = self.window, pageManager = self)
        # self.page = success.successPage(master = self.window, pageManager=self)
        # self.page = order.orderPage(master = self.window, pageManager=self)
        # self.page = product.productPage(master = self.window, pageManager = self)
        # self.page = mytransaction.myTransactionPage(master = self.window, pageManager = self)
    
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

    def __onHover__(self, event):
        event.widget.config(cursor = "hand2")

    def __onClick__(self, event):
        event.widget.invoke()

        