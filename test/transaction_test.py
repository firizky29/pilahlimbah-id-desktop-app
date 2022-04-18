import pytest
import hashlib
from datetime import datetime
import sys
import mysql.connector

from regex import R
sys.path.insert(1, "..")
import src.transaction.transaction as transaction

raw_transaction = {
    "user" : "dummy user",
    "card number" : "dummy card number",
    "bank" : "dummy bank",
    "security code" : "dummy security code",
    "address" : "dummy address",
    "city"  : "dummy city",
    "country" : "dummy country",
    "postal code" : "dummy postal code",
    "timestamp" : datetime.now(),
    "active period" : 30,
    "price" : 46000
}

class dummyPageManager():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="pilahlimbah.mariadb.database.azure.com", 
            user="pilahlimbah@pilahlimbah", 
            password="BDDL&g38Mv", 
            database = "pilahlimbahid"
        )
dummy = dummyPageManager()

def test_validateContent():
    sc = transaction.transaction(raw_transaction, dummy)
    raws = raw_transaction
    assert sc.validateContent(raws) == True

    sc.status = True
    raws = raw_transaction
    raws['card number'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['bank'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['security code'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['address'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['city'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['country'] = ""
    assert sc.validateContent(raws) == False


    sc.status = True
    raws = raw_transaction
    raws['postal code'] = ""
    assert sc.validateContent(raws) == False



def test_validateCardNumber():
    sc = transaction.transaction(raw_transaction, dummy)
    assert sc.validateCardNumber() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.cardNumber = "1111-1111-1111-1111"
    assert sc.validateCardNumber() == True

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.cardNumber = "1111-1111-11111111"
    assert sc.validateCardNumber() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.cardNumber = "1111-1111-111-1111"
    assert sc.validateCardNumber() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.cardNumber = "1111-1111-1111-A111"
    assert sc.validateCardNumber() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.cardNumber = "1111-1111-1111-11112"
    assert sc.validateCardNumber() == False


    
def test_validateSecurityCode():
    sc = transaction.transaction(raw_transaction, dummy)
    assert sc.validateSecurityCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.securityCode = "12345"
    assert sc.validateSecurityCode() == True

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.securityCode = "123456"
    assert sc.validateSecurityCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.securityCode = "A1234"
    assert sc.validateSecurityCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.securityCode = "123"
    assert sc.validateSecurityCode() == False

def test_validatePostalCode():
    sc = transaction.transaction(raw_transaction, dummy)
    assert sc.validatePostalCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.postalCode = "12345"
    assert sc.validatePostalCode() == True

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.postalCode = "123456"
    assert sc.validatePostalCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.postalCode = "A1234"
    assert sc.validatePostalCode() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.status = True
    sc.postalCode = "123"
    assert sc.validatePostalCode() == False

def test_verifyTransaction():
    sc = transaction.transaction(raw_transaction, dummy)
    assert sc.verifyTransaction() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.cardNumber = "1234-5678-9012-3456"
    sc.securityCode = "12345"
    assert sc.verifyTransaction() == True

    sc = transaction.transaction(raw_transaction, dummy)
    sc.cardNumber = "1111-1111-1111-1111"
    sc.securityCode = "12345"
    assert sc.verifyTransaction() == False

    sc = transaction.transaction(raw_transaction, dummy)
    sc.cardNumber = "1234-5678-9012-3456"
    sc.securityCode = "12346"
    assert sc.verifyTransaction() == False


