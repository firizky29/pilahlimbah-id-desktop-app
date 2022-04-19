import transaction.orderPage as order
import transaction.productPage as product
import calendarmanagement.calendarPage as calendarmanage
import akun.login as login
import akun.register as register
import akun.profile as profile
import akun.editProfile as edit
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
    
    def calendarPage(self):
        self.page = calendarmanage.calendarPage(master = self.window, pageManager = self)
        self.page.startPage()

    def loginPage(self):
        self.page = login.loginPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def registerPage(self):
        self.page = register.registerPage(master = self.window, pageManager = self)
        self.page.startPage()

    def editProfilePage(self):
        self.page = edit.editProfilePage(master = self.window, pageManager = self)
        self.page.startPage()

    def profilePage(self):
        self.page = profile.profilePage(master = self.window, pageManager = self)
        self.page.startPage()

    
