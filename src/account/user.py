
class user():
    def __init__(self, raw_user, pageManager):
        self.userInfo = pageManager.getCursor().execute(f"select * from user where username = '{raw_user[0]}'")

