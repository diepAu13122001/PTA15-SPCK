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
    def add_user(self, user: User):
        # add in course for new progress
        self.__user_list.append(user)
        self.__save_in_data()

    # read
    def search_by_username(self, username):
        for user in self.__user_list:
            if user.get_username() == username:  # Changed to get_username()
                return user
        # không tìm thấy user
        return None

    # update
    def update_user(self, updated_user: User):
        # update by username
        for i, user in enumerate(self.__user_list):
            if (
                user.get_username() == updated_user.get_username()
            ):  # Changed to get_username()
                self.__user_list[i] = updated_user
                self.__save_in_data()
                return

    # delete
    def delete_user(self, deleted_username):
        # delete by username
        for i, user in enumerate(self.__user_list):
            if user.get_username() == deleted_username:  # Changed to get_username()
                self.__user_list.pop(i)
                self.__save_in_data()
                return
