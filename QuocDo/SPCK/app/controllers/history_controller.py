from models.history import History


class HistoryController:
    def __init__(self):
        self.__history_list = self.__generate_history_list()

    # Generate an initial empty history list
    def __generate_history_list(self):
        return histories

    # Save the history list globally
    def __save_in_data(self):
        global histories
        histories = self.__history_list

    def find_best(self, email):
        if self.search_by_creator(email):
            return min(
                [float(item.get_time()) for item in self.search_by_creator(email)]
            )
        else:
            return 0

    def find_worst(self, email):
        if self.search_by_creator(email):
            return max(
                [float(item.get_time()) for item in self.search_by_creator(email)]
            )
        else:
            return 0

    # Create: Add a new history entry
    def add_history(self, history: History):
        # create id
        new_id = len(self.__history_list)
        history.set_id(new_id)
        self.__history_list.append(history)
        self.__save_in_data()

    # Read: Search history by ID
    def search_by_id(self, history_id):
        for history in self.__history_list:
            if history.get_id() == history_id:
                return history
        # History not found
        return None

    # Read: Search history by created_by (email)
    def search_by_creator(self, email):
        return [
            history
            for history in self.__history_list
            if history.get_created_by() == email
        ]

    # Update: Update a history record by ID
    def update_history(self, updated_history: History):
        for i, history in enumerate(self.__history_list):
            if history.get_id() == updated_history.get_id():
                self.__history_list[i] = updated_history
                self.__save_in_data()
                return

    # Delete: Delete a history record by ID
    def delete_history(self, history_id):
        self.__history_list = [
            history for history in self.__history_list if history.get_id() != history_id
        ]
        self.__save_in_data()


# Global variable to store history data
histories = [
    History("1", "5.07", "alice@example.com", "3x3x3"),
    History("2", "11.07", "alice@example.com", "2x2x2"),
    History("3", "5.07", "bob@example.com", "4x4x4"),
    History("4", "9.07", "alice@example.com", "3x3x3"),
    History("5", "5.07", "charlie@example.com", "3x3x3"),
    History("6", "5.07", "dave@example.com", "3x3x3"),
]
