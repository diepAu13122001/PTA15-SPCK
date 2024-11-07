from models.user import User
import dao

class UserController:
    def __init__(self):
        self.__user_list = self.__generate_user_list()
    
    # generate
    def __generate_user_list(self):
        return dao.users

    def __save_in_data(self):
        dao.users = self.__user_list
    # create
    def add_user(self, user:User):
        self.__user_list.append(user)
        self.__save_in_data()

    # read
    def search_by_username(self, username):
        for user in self.__user_list:
            if user.get_username() == username:
                return user
        # khong tim thay user
        return None

    def search_by_email(self, email):
        for user in self.__user_list:
            if user.get_email() == email:
                return user
    # update
    def update_user(self, deleted_email):
        # update by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == deleted_email:
                self.__user_list.pop(i)
                self.__save_indata()
                return

    # delete
    def detele_user(self, deleted_email):
        # delete by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == deleted_email:
                self.__user_list.pop(i)
                self.__save_in_data()
                return
    