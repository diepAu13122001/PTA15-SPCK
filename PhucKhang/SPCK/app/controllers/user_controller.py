from models.user import User
import dao
from controllers.course_controller import CourseController

class UserController:
    def __init__(self):
        self.__user_list = self.__generate_user_list()
        
    #generate
    def __generate_user_list(self):
        return dao.users

    def __save_in_data(self):
        dao.users = self.__user_list

    #create
    def add_user(self, user:User):
        #  add in course for new progress
        courseController = CourseController()
        courseController.add_courses_for_new_user(user.get_email())
        self.__user_list.append(user)
        self.__save_in_data()

    #read
    def search_by_email(self, email):
        for user in self.__user_list:
            if user.get_email() == email:
                return user
        #khong tim thay user
        return None

    

        #khong tim thay user
        return None
    #update

    def update_user(self, updated_user:User):
        #update by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == updated_user.get_email():
                self.__user_list[i] = updated_user
                self.__save_in_data()
                return

        
        # delete
    def delete_user(self, deleted_email):
        #delete by email
        for i, user in enumerate(self.__user_list):
            if user.get_email() == deleted_email:
                self.__user_list.pop(i)
                self.__save_in_data()
                return

    
