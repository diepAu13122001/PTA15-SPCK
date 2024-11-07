import sys
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from controllers.user_controller import UserController
from models.user import User
from views.home import Home


class Signup(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.ui = uic.loadUi(self.root_ui_path + "signup.ui", self)
        self.setWindowTitle("signup")

        # Handle button click events
        self.login_btn.clicked.connect(self.goto_login)
        self.signup_btn.clicked.connect(self.check_signup)

    def validate_form(self, username, password, confirmPassword):
        # Check for empty fields
        if not (username and password and confirmPassword):
            self.show_message("Please fill out all the fields in this form!")
            return False
        if len(password) < 6:
            self.show_message(
                "The password is too short! Password should have at least 6 characters"
            )
            return False
        if confirmPassword != password:
            self.show_message("Passwords do not match!")
            return False
        return True

    def check_signup(self):
        # Get data from line edits
        username = self.username.text()
        password = self.password.text()
        confirmPassword = self.confirmPassword.text()

        # Validate form data
        if self.validate_form(
            username=username, password=password, confirmPassword=confirmPassword
        ):
            # Check for duplicate username
            userController = UserController()
            found_user = userController.search_by_username(username)
            if found_user:
                self.show_message(
                    "Username is in use. Please sign in or try another username."
                )
                return
            new_user = User(username=username, password=password)
            userController.add_user(new_user)

            # Transition to home
            try:
                home = Home(self.root_ui_path, currentUsername=username)
                home.show()
                self.close()
            except Exception as e:
                print(e)

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        ok_button.setStyleSheet("background-color: #598896;")
        msg_box.exec()

    def goto_login(self):
        from views.login import Login

        login = Login(self.root_ui_path)
        login.show()
        self.close()
