class User:
    # Khai báo thuộc tính cần thiết cho user
    def __init__(self, username, email, password):
        # Khai báo biến dưới dạng private "__"
        self.__username = username
        self.__email = email
        self.__password = password

    # Getter + setter ( tính đóng gói OOP)
    def set_username (self, username):
        self.__username = username

    def set_email (self, email):
        self.__email = email

    def set_password (self, password):
        self.__password = password

    def get_username (self):
        return self.__username

    def get_email (self ):
        return self.__email

    def get_password (self):
        return self.__password