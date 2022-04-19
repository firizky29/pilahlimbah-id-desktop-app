
import hashlib
from datetime import datetime, timezone

import pytz

class user():
    def __init__(self, raw_user, pageorigin):
        self.origin = pageorigin
        self.status = True
        self.warning = ""
        self.role = None

        if(len(raw_user)==2):
            # kalau login
            self.username = raw_user[0]
            self.password = raw_user[1]
            # lakukan validasi input dulu, kalau inputnya kosong, self warningnya ganti jadi pesan error, self statusnya jadi False
            self.validateInputLogin()
            
            if(self.status):
                # kalau udah validasi:
                self.verifyLogin()

                # Kalau udah verified
                self.fullname = ''
                self.email = ''
                self.birthdate = ''
                self.gender = ''
                self.address = ''
                self.city = ''
                self.country = ''
                self.postalCode = ''

                self.regionId = ''
                self.userId = ''
                self.deadline = ''
                
                if(self.status):
                    self.commitLogin()
        else:
            # kalau register
            self.username = raw_user[0]
            self.password = raw_user[1]
            self.fullname = raw_user[2]
            self.email = raw_user[3]
            self.birthdate = raw_user[4]
            self.gender = raw_user[5]
            self.address = raw_user[6]
            self.city = raw_user[7]
            self.country = raw_user[8]
            self.postalCode = raw_user[9]

            self.regionId = 'NULL'
            self.userId = ''

            self.verifyRegister()
            self.commitRegister()
            # lakukan validasi input, boleh cek di modul transaction/transaction.py, cara validasinya mirip itu
            # contoh validasi: email harus ada @, nama gaboleh angka, 
            # ubah self.warning kalau gagal jadi pesan error, dan self statusnya jadi False
        
        if(self.status):
            self.getUserID()
        
        
    def validateInputLogin(self):
        if(self.username == '' or self.password == ''):
            self.status = False
            if(self.username == ''):
                self.warning = 'username must not empty'
            else:
                self.warning = 'password must not empty'
            return False
        return True

    def verifyLogin(self):
        # verify beda sama validasi.
        # verify itu ngecek usernamenya ada/nggak di database
        # kalau ada, dan hashlib.sha256(self.password.encode()).hexdigest() == password di database, berarti aman
        # update self status dan self warning kalau error
        user_info = self.origin.mydb.cursor(buffered = True)
        user_info.execute(f"select * from user where username = '{self.username}'")
        if(user_info.rowcount == 0):
            if(not(self.status)):
                self.warning = 'username is not valid'
            self.status = False
            return False
        user_info = user_info.fetchone()
        if(hashlib.sha256(self.password.encode()).hexdigest() != user_info[2]):
            if(not(self.status)):
                self.warning = 'password is not valid'
            self.status = False
            return False
        return True

    def verifyRegister(self):
        # ini proses masukin info user ke database.
        # cara insertnya:
        # insert region-nya dulu (kalau input region kosong, skip aja), (region_id isi 0 aja)
        if('INI ISI YA KONDISIONALNYA' == True):
            region_info = self.origin.mydb.cursor(buffered=True)
            region_info.execute(f"select region_id from region where region = '{self.address}' and city = '{self.city}' and country = '{self.country}' and postal_code = '{self.postalCode}'")
            if(region_info.rowcount == 0):
                self.origin.mydb.cursor().execute(f"insert into region values (0, '{self.address}', '{self.city}', '{self.country}', '{self.postalCode}')")
                self.origin.mydb.commit()

                region_info = self.origin.mydb.cursor(buffered=True)
                region_info.execute(f"select region_id from region where region = '{self.address}' and city = '{self.city}' and country = '{self.country}' and postal_code = '{self.postalCode}'")
            self.regionId = region_info.fetchone()[0]

        # insert user (roles set null dulu, user_id set 0 aja)
        return

    def getUserID(self):
        # PASTIIN INI CUMA DIPANGGIL KALAU USER_ID UDAH DIDAFTARIN SETELAH VERIFY REGISTER
        user_id = self.origin.mydb.cursor(buffered = True)
        user_id.execute(f"select user_id from user where username = '{self.username}'")

        self.userId = user_id.fetchone()[0]

        
    def commitRegister(self):
        # ini proses masukin role
        # caranya:
        # langsung insert guest aja, guest_id nya self.getUserID(). region_id isi sama self.regionId
        return

    def commitLogin(self):
        user_info = self.origin.mydb.cursor(buffered=True)
        user_info.execute(f"select * from user where username = '{self.username}'")
        user_info = user_info.fetchone()
        self.userId = user_info[0]
        self.email = user_info[3]
        self.fullname = user_info[4]
        self.birthdate = user_info[5]
        self.gender = user_info[6]
        self.role = user_info[7]


        region_info = self.origin.mydb.cursor(buffered=True)
        proj = "region_id, region, city, country, postal_code"
        if(self.role == 'Admin'):
            region_info.execute(f"select {proj} from user join admin natural inner join region where user.user_id = admin.admin_id")
        elif(self.role == 'Member'):
            region_info.execute(f"select {proj} from user join member natural inner join region where user.user_id = member.member_id")
        elif(self.role == 'Guest'): 
            region_info.execute(f"select {proj} from user join guest natural inner join region where user.user_id = guest.guest_id")

        if(region_info.rowcount > 0):
            region_info = region_info.fetchone()
            self.regionId = region_info[0]
            self.address = region_info[1]
            self.city = region_info[2]
            self.country = region_info[3]
            self.postalCode = region_info[4]

        if(self.role == 'Member'):
            orderlist = self.origin.mydb.cursor(buffered = True)
            table = "orderlist as ol inner join account as ac on ol.account_id = ac.account_id"
            orderlist.execute(f"select deadline_date from {table} where user_id = {self.userId} order by deadline_date desc limit 1")
            if(orderlist.rowcount > 0):
                self.deadline = orderlist.fetchone()[0].replace(tzinfo=timezone.utc)
                if(self.deadline < datetime.now(pytz.utc)):
                    self.changeRole('Guest')    



    def changeRole(self, newRole, transaction = None):
        if(transaction):
            region_info = self.origin.mydb.cursor(buffered=True)
            region_info.execute(f"select region_id from region where region = '{transaction.address}' and city = '{transaction.city}' and country = '{transaction.country}' and postal_code = '{transaction.postalCode}'")
            if(region_info.rowcount == 0):
                self.origin.mydb.cursor().execute(f"insert into region values (0, '{transaction.address}', '{transaction.city}', '{transaction.country}', '{transaction.postalCode}')")
                self.origin.mydb.commit()

                region_info = self.origin.mydb.cursor(buffered=True)
                region_info.execute(f"select region_id from region where region = '{transaction.address}' and city = '{transaction.city}' and country = '{transaction.country}' and postal_code = '{transaction.postalCode}'")

            self.origin.mydb.cursor().execute(f"insert into member values ({self.userId},{region_info.fetchone()[0]})")
            self.origin.mydb.commit()
        else:
            self.origin.mydb.cursor().execute(f"delete from member where member_id = {self.userId}")
            self.origin.mydb.commit()

        self.role = newRole

