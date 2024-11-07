from models.motor import Motor  # Assuming Motor is defined in models.motor
import dao  # Assuming dao handles data storage for motors


class MotorController:
    def __init__(self):
        # Initialize motor list by calling a private method to generate it from dao
        self.__motor_list = self.__generate_motor_list()

    # Private method to generate the initial list of motors from dao
    def __generate_motor_list(self):
        return dao.motors  # Assuming dao.motors holds initial motor data

    # Private method to save the motor list to dao
    def __save_in_data(self):
        dao.motors = self.__motor_list
    
    def get_all_motors(self):
        return self.__motor_list

    # Create: Add a new motor to the list
    def add_motor(self, motor: Motor):
        self.__motor_list.append(motor)
        self.__save_in_data()

    # Read: Search motor by name
    def search_by_name(self, name):
        for motor in self.__motor_list:
            if name in motor.get_name():
                return motor
        # Return None if motor is not found
        return None

    # Read: Search motor by ID
    def search_by_id(self, motor_id):
        for motor in self.__motor_list:
            if motor.get_id() == motor_id:
                return motor
        # Return None if motor is not found
        return None

    # Update: Update a motor’s data by its ID
    def update_motor(self, motor_id, updated_motor: Motor):
        for i, motor in enumerate(self.__motor_list):
            if motor.get_id() == motor_id:
                self.__motor_list[i] = updated_motor
                self.__save_in_data()
                return True
        return False  # Return False if motor to update is not found

    # Delete: Delete a motor from the list by its ID
    def delete_motor(self, motor_id):
        for i, motor in enumerate(self.__motor_list):
            if motor.get_id() == motor_id:
                self.__motor_list.pop(i)
                self.__save_in_data()
                return True
        return False  # Return False if motor to delete is not found