from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os
from controllers.user_controller import UserController
from views.home import Home
from models.user import User


class Signup(QMainWindow):
    def __init__(self, root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.ui = uic.loadUi(self.root_ui_path + "signup.ui", self)
        self.setWindowTitle("Signup")

        # bat su kien cho cac btn
        self.login_btn.clicked.connect(self.goto_login)
        self.signup_btn.clicked.connect(self.check_singup)

    def validate_from(self, username, email, password, confirmPassword):
        # du lieu bi rong
        if not (email and username and password and confirmPassword):
            self.show_message("nhap lai di kuuu!!!!")
        if len(username) < 3 or not username.isalnum():
            self.show_message("nhap lai di kuu!!!!")
            return False
        if len(password) < 6:
            self.show_message("nhap lai di ku!!!!")
            return False
        if confirmPassword != password:
            self.show_message("ac thuuc lai mk di kuu!!!!")
            return False
        return True

    def check_singup(self):
        # lay duu lieu tu line edit
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        confirmPassword = self.confirmPassword.text()

        # kiem tra from
        if self.validate_from(
            username=username,
            email=email,
            password=password,
            confirmPassword=confirmPassword,
        ):
            # kiem tra username + passwoed da ton tai
            userController = UserController()
            found_user = userController.search_by_username(username)
            # trung username
            if found_user:
                self.show_message("nhap lai username di ku!!!!")
                return
            found_user = userController.search_by_email(email)
            # truung email
            if found_user:
                self.show_message("nhap lai email di ku!!!!")
                return

            # add vao data
            try:
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
