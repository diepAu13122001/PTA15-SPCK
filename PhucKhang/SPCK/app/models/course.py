class Course:
    # Initialize Course with private id, icon, name, and process attributes
    def __init__(self, course_id, icon, name):
        self.__id = course_id
        self.__icon = icon
        self.__name = name
        self.__process = {}

    # Getter and setter for id
    def get_id(self):
        return self.__id
    
    def set_id(self, course_id):
        self.__id = course_id

    # Getter and setter for icon
    def get_icon(self):
        return self.__icon
    
    def set_icon(self, icon):
        self.__icon = icon

    # Getter and setter for name
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    # Getter and setter for user progress
    def get_user_progress(self, user_email):
        return self.__process.get(user_email, 0)
    
    def set_user_progress(self, user_email, progress):
        if 0 <= progress <= 100:
            self.__process[user_email] = progress
        else:
            raise ValueError("Progress must be between 0 and 100")

    # Method to get all user progress
    def get_all_progress(self):
        return self.__process
