import pytz
import transaction.orderPage as order
import transaction.productPage as product
import calendarmanagement.calendarPage as calendarmanage
import transaction.myTransactionPage as mytransaction
import transaction.successPage as success
import transaction.transaction as transaction
import transaction.transactionDetailsPage as transactionDetails
import account.user as account
import mysql.connector
from datetime import datetime
from tkinter import Tk


class pageManager():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="pilahlimbah.mariadb.database.azure.com", 
            user="pilahlimbah@pilahlimbah", 
            password="BDDL&g38Mv", 
            database = "pilahlimbahid"
        )

        self.user = account.user(['pilahlimbahid', 'pilahlimbahid'], self)
        self.window = Tk()
        self.window.geometry("1080x700")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Enter>", self.__onHover__)
        self.window.bind_class("Button", "<Button-1>", self.__onClick__)
        # inisialisasi dengan page login/register, tapi sementara pake page product dulu
        # self.page = transactionDetails.transactionDetailsPage(master = self.window, pageManager = self)
        # self.page = success.successPage(master = self.window, pageManager=self)
        self.page = order.orderPage(master = self.window, pageManager=self)
        # self.page = product.productPage(master = self.window, pageManager = self)
        # self.page = mytransaction.myTransactionPage(master = self.window, pageManager = self)
        # self.page = order.orderPage(master = self.window, pageManager=self)
    
    def checkMembership(self):
        if(self.user.deadline < datetime.now(pytz.utc)):
            self.user.changeRole('Guest')   

    def run(self):
        self.page.startPage()

    def setUser(self, user):
        self.user = user

    def orderPage(self):
        self.checkMembership()
        self.page = order.orderPage(master = self.window, pageManager = self)
        self.page.startPage()

    def productPage(self):
        self.checkMembership()
        self.page = product.productPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def calendarPage(self):
        self.page = calendarmanage.calendarPage(master = self.window, pageManager = self)
        self.page.startPage()

    

    def successPage(self, transaction):
        self.checkMembership()
        self.page = success.successPage(master = self.window,  pageManager = self, transaction = transaction)
        self.page.startPage()
    
    def transactionDetails(self, transaction):
        self.checkMembership()
        self.page = transactionDetails.transactionDetailsPage(master = self.window,  pageManager = self, transaction = transaction)
        self.page.startPage()

    def myTransaction(self):
        self.checkMembership()
        self.page = mytransaction.myTransactionPage(master = self.window, pageManager = self)
        self.page.startPage()

    def __onHover__(self, event):
        event.widget.config(cursor = "hand2")

    def __onClick__(self, event):
        event.widget.invoke()

        
