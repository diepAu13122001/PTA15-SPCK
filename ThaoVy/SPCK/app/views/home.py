from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
import os


# tao class de chua giao dien
class Home(QMainWindow):
    def __init__(self, root_ui_path, currentUsername):
        super().__init__()
        # ket noi giao dien voi code
        self.ui = uic.loadUi(root_ui_path + "home.ui", self)

        # event for search button
        self.search_btn.clicked.connect(self.search)
        # event for buttons to change stacks
        self.meals_btn.clicked.connect(self.show_page_1)
        self.fastoods_btn.clicked.connect(self.show_page_2)
        self.heathyfood_btn.clicked.connect(self.show_page_3)

    def show_page_1(self):
        self.food_stacked.setCurrentIndex(0)

    def show_page_2(self):
        self.food_stacked.setCurrentIndex(2)

    def show_page_3(self):
        self.food_stacked.setCurrentIndex(1)

    def search(self):
        pass
