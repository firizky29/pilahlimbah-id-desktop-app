
import re
import mysql.connector

class transaction():
    def __init__(self, raw_transaction):
        mysqldb = mysql.connector.connect(
            host="pilahlimbah.mariadb.database.azure.com", 
            user="pilahlimbah@pilahlimbah", 
            password="BDDL&g38Mv", 
            database = "pilahlimbahid"
        )
        sqlcursor = mysqldb.cursor()
        sqlcursor.execute("SELECT * FROM task limit 5")
        for i in sqlcursor:
            print(i)
        self.user = raw_transaction["user"]
        self.cardNumber = raw_transaction['card number']
        self.bank = raw_transaction['bank']
        self.securityCode = raw_transaction['security code']
        self.address = raw_transaction["address"]
        self.city = raw_transaction['city']
        self.country = raw_transaction['country']
        self.postalCode = raw_transaction['postal code']
        self.timeStamp = raw_transaction['timestamp']
        self.activePeriod = raw_transaction['active period']
        self.status = True
        self.warning = ""
        self.validateCard()
        for key in raw_transaction:
            print(key, "->", raw_transaction[key])
            if(self.status and key!="user" and key!="timestamp" and key!= "active period" and len(raw_transaction[key])==0):
                self.warning = key + " must not empty"
                self.status = False

        self.validatePostalCode()

    def validateCardNumber(self):
        if(not(self.status) or len(self.cardNumber)!=19 or re.search(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", self.cardNumber)==None):
            if(self.status):
                self.warning = "Your card number is not valid"
            self.status = False
    
    def validateSecurityCode(self):
        if(not(self.status) or re.search(r"[0-9]{5}", self.securityCode)==None):
            if(self.status):
                self.warning = "Security code is not valid"
            self.status = False

    def validatePostalCode(self):
        if(not(self.status) or re.search(r"[0-9]{5}", self.postalCode)==None):
            if(self.status):
                self.warning = "Postal code is not valid"
            self.status = False

    def validateCard(self):
        self.validateCardNumber()
        self.validateSecurityCode()

    def getWarning(self):
        return self.warning