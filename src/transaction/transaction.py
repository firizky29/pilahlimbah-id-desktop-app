
import re

from sympy import false


class transaction():
    def __init__(self, raw_transaction, pageManager):
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
        self.status = True
        self.warning = ""
        self.validateCard()
        for key in raw_transaction:
            if(self.status and key!="user" and key!="timestamp" and key!= "active period" and key != 'price' and len(raw_transaction[key])==0):
                if(key == "bank"):
                    self.warning = "Your card is not registered in any bank account"
                else:
                    self.warning = key + " must not empty"
                self.status = False

        self.validatePostalCode()
        if(self.status):
            self.verifyTransaction()

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

    def verifyTransaction(self):
        input_account = self.cardNumber.replace("-", "")
        credit_infos = self.origin.mydb.cursor(buffered=True)
        credit_infos.execute(f"select * from account where account_number = '{input_account}'")
        if(credit_infos.rowcount==0):
            self.warning = "Invalid card number"
            self.status = false
            return
        credit_info = credit_infos.fetchone()
        if(self.securityCode != credit_info[3]):
            self.warning = "Invalid security code"
            self.status = false
            return
        if(credit_info[5] < self.price):
            self.warning = "Your card balance is not enough"
            self.status = false
            return
        self.origin.mydb.cursor().execute(f"insert into orderlist values (0, '{credit_info[0]}', SYSDATE(), SYSDATE(), {self.price})")
        self.origin.mydb.commit()
        


        

