from models.user import User


class UserController:
    def __init__(self):
        self.__user_list = self.__generate_uset_list()

    #generate
    def __generate_uset_list(self):
        return users
    
    def __save_in_data(self):
        global users
        users = self.__user_list
    #create
    def add_user(self, user:User):
        self.__user_list.append(user)
        self.__save_in_data()

    #read
    def search_by_username(self, username):
        for user in self.__user_list:
            if user.get_username( ) == username:
                return user
        # khong tim thay user
        return None
    
    def search_by_email(self, email):
        for user in self.__user_list:
            if user.get_email( ) == email:
                return user
        # khong tim thay user
        return None
    #update
    def update_user(self,updated_user:User):
        #uupdate by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == updated_user.get_email():
                self.__user_list[i] = updated_user
                self.__save_in_data()
                return
            
    #delete
    def delete_user(self,delete_email:User):
        #delete by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == delete_email:
                self.__user_list.pop(i)
                self.__save_in_data()
                return
            


users = [
    User("alice", "alice@example.com", "alice123"),
    User("bob", "bob@example.com", "bob456"),
    User("charlie", "charlie@example.com", "charlie789"),
    User("dave", "dave@example.com", "dave1011"),
    User("eve", "eve@example.com", "eve1213")
]