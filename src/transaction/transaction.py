
import re
from datetime import datetime, timedelta
import hashlib

class transaction():
    def __init__(self, raw_transaction, pageManager = None):
        if(pageManager == None):
            self.cardNumber = raw_transaction['card number']
            self.bank = raw_transaction['bank']
            self.timeStamp = raw_transaction['timestamp']
            self.price = raw_transaction['price']
            self.deadline = raw_transaction['deadline']
        else:
            self.origin = pageManager
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
            self.price = raw_transaction['price']
            self.deadline = self.timeStamp + timedelta(days=self.activePeriod)
            self.status = True
            self.warning = ""
            self.validateCard()
            self.validateContent(raw_transaction)
            self.validatePostalCode()
            if(self.status):
                self.verifyTransaction()
    
        
    def validateContent(self, raw_transaction):
        for key in raw_transaction:
            if(self.status and key!="user" and key!="timestamp" and key!= "active period" and key != 'price' and len(raw_transaction[key])==0):
                if(key == "bank"):
                    self.warning = "Your card is not registered in any bank account"
                else:
                    self.warning = key + " must not empty"
                self.status = False
                return False
        return True

    def validateCardNumber(self):
        if(not(self.status) or len(self.cardNumber)!=19 or re.search(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", self.cardNumber)==None):
            if(self.status):
                self.warning = "Your card number is not valid"
            self.status = False
            return False
        return True
    
    def validateSecurityCode(self):
        if(not(self.status) or len(self.securityCode) != 5 or re.search(r"[0-9]{5}", self.securityCode)==None):
            if(self.status):
                self.warning = "Security code is not valid"
            self.status = False
            return False
        return True

    def validatePostalCode(self):
        if(not(self.status) or len(self.postalCode) != 5 or re.search(r"[0-9]{5}", self.postalCode)==None):
            if(self.status):
                self.warning = "Postal code is not valid"
            self.status = False
            return False
        return True

    def validateCard(self):
        self.validateCardNumber()
        self.validateSecurityCode()

    def getWarning(self):
        return self.warning

    def verifyTransaction(self):
        input_account = self.cardNumber.replace("-", "")
        credit_infos = self.origin.mydb.cursor(buffered=True)
        credit_infos.execute(f"select * from account where account_number = '{input_account}'")
        if(credit_infos.rowcount==0):
            self.warning = "Invalid card number"
            self.status = False
            return False
        credit_info = credit_infos.fetchone()
        hashedSecurityCode = hashlib.sha256(self.securityCode.encode()).hexdigest()
        if(hashedSecurityCode != credit_info[3]):
            self.warning = "Invalid security code"
            self.status = False
            return False
        if(credit_info[5] < self.price):
            self.warning = "Your card balance is not enough"
            self.status = False
            return False
        self.origin.mydb.cursor().execute(f"insert into orderlist values (0, '{credit_info[0]}', SYSDATE(), SYSDATE() + interval '{self.activePeriod}' day, {self.price})")
        self.origin.mydb.commit()
        return True
        


        

