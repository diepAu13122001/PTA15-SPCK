
class User:
    # khai bao thuoc tinh can cho object user
    def __init__(self, username, email, password):
    # khai bao bien duoi dang private ''--''
        self.__username = username
        self.__email = email
        self.__password = password

    # getter + setter (tinh dang goi OOP)
    def set_username(self,username):
        self.__username = username

    def set_email(self,email):
        self.__email = email

    def set_password(self,password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password