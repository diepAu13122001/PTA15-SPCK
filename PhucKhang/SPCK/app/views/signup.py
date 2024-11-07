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

        #bat su kien cho cac pushbutton
        self.login_btn.clicked.connect(self.goto_login)
        #self.login_btn.mousePressEvent = self.goto_login
        self.signup_btn.clicked.connect(self.check_signup)

    def validate_form(self, email, password, confirmPassword):
        #du lieu bi rong
        if not (email and password and confirmPassword):
            self.show_message("Please fill out all the fields in this form!")
            return False
        if len(password) < 6:
            self.show_message("The password is too short! Password should have at least 6 characters")
            return False
        if confirmPassword != password:
            self.show_message("Passwords do not match!")
            return False
        return True

    def check_signup(self):
        #Lay du lieu tu cac line edit
        email=self.email.text()
        password = self.password.text()
        confirmPassword = self.confirmPassword.text()
        #kiem tra form
        if self.validate_form(email=email, password=password, confirmPassword=confirmPassword):
        # trung email
            userController = UserController()
            found_user = userController.search_by_email(email)
            if found_user:
                self.show_message("Email is in use. Please sign in or try another email")
                return
            new_user = User(email=email, password=password)
            userController.add_user(new_user)
        # chuyen sang home
            home = Home(self.root_ui_path, currentUserEmail=email)
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

    def goto_login(self):
        from views.login import Login
        login = Login(self.root_ui_path)
        login.show()
        self.close()