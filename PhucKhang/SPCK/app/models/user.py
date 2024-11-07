class User:
    # khai bao thuoc tinh can cho object user
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def set_username(self, email):
        self.__email = email

    def set_username(self, password):
        self.__password = password

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password
