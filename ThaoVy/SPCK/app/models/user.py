class User:
    def __init__(self, username, password):
        # Private attributes
        self.__username = username
        self.__password = password

    # Getter and Setter for username
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    # Getter and Setter for password
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
