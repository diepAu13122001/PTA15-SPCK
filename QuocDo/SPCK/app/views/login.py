from PyQt6.QtWidgets import QApplication , QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os
from controllers.user_controller import UserController
from views.home import Home
from models.user import User

class Login(QMainWindow):
    def __init__(self,root_ui_path):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.ui = uic.loadUi(self.root_ui_path + "login.ui", self)
        self.setWindowTitle('login')

        # bat su kien cho cac btn
        self.login_btn.clicked.connect(self.check_login)
        self.signup_btn.clicked.connect(self.goto_signup)

    def validate_from(self, email, password):
        # du lieu bi rong
        if not(email and password):
            self.show_message('loii!!!!')
            return False
        return True
    def check_login(self):
        # lay du lieu tu cac line edot 
        email = self.email.text()
        password = self.password.text()
        # kiem tra form 
        if self.validate_from(email=email, password=password):
            # kiem tra username + email da ton tai
            try: 
                userController = UserController()
                found_user = userController.search_by_email(email)
                # tim bang email
                if found_user:
                    if password != found_user.get_password():
                        self.show_message("Your password is not match")
                        return
                    else:
                        # chuyen sang home
                        home = Home(self.root_ui_path, currentUserEmail=email)
                        home.show()
                        self.close()
                else:
                    self.show_message('Tai khoan khong ton tai')
                    return
            except Exception as e:
                print(e)
    def show_message(self,message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.addButton(QMessageBox.StandardButton.Ok)
        ok_button.setStyleSheet("background-color: #598896;")
        msg_box.exec()

    def goto_signup(self):
        from views.signup import Signup
        try:
            signup = Signup(self.root_ui_path)
            signup.show()
            self.close()
        except Exception as e:
            print(e)