import pytz
import transaction.orderPage as order
import transaction.productPage as product
import mycalendar.calendarPage as mycal
import transaction.myTransactionPage as mytransaction
import transaction.successPage as success
import transaction.transaction as transaction
import transaction.transactionDetailsPage as transactionDetails
import account.user as account
import dashboard.DashboardUserPage as dashboarduser
import dashboard.DashboardAdminPage as dashboardadmin
import dashboard.TipsAndTricksPage as tipsAndTricks
import account.editProfile as editProfile
import account.login as login
import account.register as register
import account.profile as profile
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

        # self.user = account.user(['pilahlimbahid', 'pilahlimbahid'], self)
        self.user = None
        self.window = Tk()
        self.window.geometry("1080x700")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Enter>", self.__onHover__)
        self.window.bind_class("Button", "<Button-1>", self.__onClick__)
        # inisialisasi dengan page login/register, tapi sementara pake page product dulu
        # self.page = transactionDetails.transactionDetailsPage(master = self.window, pageManager = self)
        # self.page = success.successPage(master = self.window, pageManager=self)
        # self.page = order.orderPage(master = self.window, pageManager=self)
        # self.page = product.productPage(master = self.window, pageManager = self)
        # self.page = mycal.calendarPage(master = self.window, pageManager = self)
        # self.page = product.productPage(master = self.window, pageManager = self)
        # self.page = order.orderPage(master = self.window, pageManager=self)
        # self.page = dashboarduser.DashboardUserPage(master = self.window, pageManager = self)
        self.page = login.loginPage(master = self.window, pageManager = self)
        # self.page = register.registerPage(self.window, self)
        # self.page = profile.profilePage(self.window, self)
        # self.page = dashboardadmin.DashboardAdminPage(master = self.window, pageManager = self)
        # self.page = mytransaction.myTransactionPage(master = self.window, pageManager = self)
        # self.page = tipsAndTricks.TipsAndTricksPage(self.window, self)
    def checkMembership(self):
        if(self.user.role == 'Member'):
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
        if(self.user.role == 'Guest'):
            self.page = dashboarduser.DashboardUserPage(master = self.window, pageManager = self)
        else:
            self.page = mycal.calendarPage(master = self.window, pageManager = self)
        self.page.startPage()

    def loginPage(self):
        self.page = login.loginPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def registerPage(self):
        self.page = register.registerPage(master = self.window, pageManager = self)
        self.page.startPage()

    def editProfilePage(self):
        self.page = editProfile.editProfilePage(master = self.window, pageManager = self)
        self.page.startPage()

    def profilePage(self):
        self.page = profile.profilePage(master = self.window, pageManager = self)
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

    def homePage(self):
        if(self.user.role == 'Admin'):
            self.page = dashboardadmin.DashboardAdminPage(master = self.window, pageManager = self)
        else:
            self.page = dashboarduser.DashboardUserPage(master = self.window, pageManager = self)
        self.page.startPage()

    def tipsAndTricksPage(self):
        if(self.user.role == 'Guest'):
            self.page = dashboarduser.DashboardUserPage(master = self.window, pageManager = self)
        else:
            self.page = tipsAndTricks.TipsAndTricksPage(master = self.window, pageManager = self)
        self.page.startPage()

    def __onHover__(self, event):
        event.widget.config(cursor = "hand2")

    def __onClick__(self, event):
        event.widget.invoke()
