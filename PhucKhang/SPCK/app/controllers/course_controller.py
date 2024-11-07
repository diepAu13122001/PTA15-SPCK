from models.course import Course
import dao


class CourseController:
    def __init__(self):
        self.__course_list = self.__generate_course_list()

    # Generate course list from dao
    def __generate_course_list(self):
        return dao.courses

    # Save the current course list back to dao
    def __save_in_data(self):
        dao.courses = self.__course_list

    def get_all_courses(self):
        return self.__course_list

    def get_courses_by_email(self, user_email):
        # Dictionary to store course progress with course_id as the key
        user_courses = {}

        # Iterate through each course and check if user has progress recorded
        for course in self.__course_list:
            progress = course.get_user_progress(user_email)
            if isinstance(
                progress, int
            ):  # Ensure the user is enrolled (progress is an integer)
                user_courses[course.get_id()] = progress

        return user_courses

    #  Create
    def add_course(self, course: Course):
        self.__course_list.append(course)
        self.__save_in_data()

    # Read - search course by name
    def search_by_name(self, name):
        for course in self.__course_list:
            if course.get_name() == name:
                return course
        # Course not found
        return None

    # Update - update a course by id
    def update_course(self, updated_course: Course):
        for i, course in enumerate(self.__course_list):
            if course.get_id() == updated_course.get_id():
                self.__course_list[i] = updated_course
                self.__save_in_data()
                return
    
    def add_courses_for_new_user(self, userEmail):
        for i, course in enumerate(self.__course_list):
            course.set_user_progress(user_email=userEmail, progress=0)
            self.__course_list[i] = course
        self.__save_in_data()

    # Delete - delete a course by id
    def delete_course(self, course_id):
        for i, course in enumerate(self.__course_list):
            if course.get_id() == course_id:
                self.__course_list.pop(i)
                self.__save_in_data()
                return
