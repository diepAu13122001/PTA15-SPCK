import sys
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from controllers.user_controller import UserController
from views.home import Home
from models.user import User
from views.signup import Signup


class Login(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.ui = uic.loadUi(self.root_ui_path + "login.ui", self)
        self.setWindowTitle("Login")

        # Handle button click events
        self.login_btn.clicked.connect(self.check_login)
        self.signup_btn.clicked.connect(self.goto_signup)

    def validate_form(self, username, password):
        # Check for empty fields
        if not (username and password):
            self.show_message("Please fill all the fields in this form!")
            return False
        return True

    def check_login(self):
        # Get data from line edits
        username = self.username.text()
        password = self.password.text()

        # Validate form data
        if self.validate_form(username=username, password=password):
            # Check for existing username
            userController = UserController()
            found_user = userController.search_by_username(username)
            print(found_user)

            # Find user by username
            if found_user:
                if password != found_user.get_password():
                    self.show_message("Your password is incorrect")
                    return
                else:
                    # Transition to home
                    home = Home(self.root_ui_path, currentUsername=username)
                    home.show()
                    self.close()

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        ok_button.setStyleSheet("background-color: #598896;")
        msg_box.exec()

    def goto_signup(self):
        signup = Signup(self.root_ui_path)
        signup.show()
        self.close()
