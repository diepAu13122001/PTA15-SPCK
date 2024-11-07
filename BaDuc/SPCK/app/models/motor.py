class Motor:
    # Initialize the Motor object with id, name, img, publish_year, and type attributes
    def __init__(self, id, name, img, publish_year, motor_type):
        # Declare private attributes with '__'
        self.__id = id
        self.__name = name
        self.__img = img
        self.__publish_year = publish_year
        self.__motor_type = motor_type

    # Getter and Setter for id
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    # Getter and Setter for name
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # Getter and Setter for img
    def set_img(self, img):
        self.__img = img

    def get_img(self):
        return self.__img

    # Getter and Setter for publish_year
    def set_publish_year(self, publish_year):
        self.__publish_year = publish_year

    def get_publish_year(self):
        return self.__publish_year

    # Getter and Setter for motor_type
    def set_motor_type(self, motor_type):
        self.__motor_type = motor_type

    def get_motor_type(self):
        return self.__motor_type