import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
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

        # bat su kien cho cac pushbutton
        self.login_btn.clicked.connect(self.goto_login)
        # self.login_btn.mousePressEvent = self.goto_login
        self.signup_btn.clicked.connect(self.check_signup)

    def validate_form(self, username, email, password, confirmPassword):
        # du lieu bi rong
        if not (email and username and password and confirmPassword):
            self.show_message("Please fill all the field in this form!")
            return False
        if len(username) < 3 or not username.isalnum():
            self.show_message(
                "Username needs has least 3 characters (no special symbol)"
            )
            return False
        if len(password) < 6:
            self.show_message("Password needs has least 6 characters!")
            return False
        if confirmPassword != password:
            self.show_message("Password and confirm password is not matching!")
            return False
        return True

    def check_signup(self):
        try:
            # lay du lieu tu cac line edot
            username = self.username.text()
            email = self.email.text()
            password = self.password.text()
            confimPassword = self.confimPassword.text()
            # kiem tra form
            if self.validate_form(
                username=username,
                email=email,
                password=password,
                confirmPassword=confimPassword,
            ):

                # kiem tra username + email da ton tai
                userController = UserController()
                found_user = userController.search_by_username(username)
                # trung username
                if found_user:
                    self.show_message(
                        "Username is aready exist, please signin or change your username!"
                    )
                    return
                found_user = userController.search_by_email(email)
                # trung email
                if found_user:
                    self.show_message(
                        "Email is aready exist, please signin or change your Email!"
                    )
                    return
                # add vao data
                new_user = User(username=username, email=email, password=password)
                userController.add_user(new_user)
                # chuyen sang home
                home = Home(self.root_ui_path, currentUserEmail=email)
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
