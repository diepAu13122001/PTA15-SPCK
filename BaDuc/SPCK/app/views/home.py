import sys
import os
from PyQt6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
)
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from controllers.motor_controller import MotorController


class Home(QMainWindow):
    def __init__(self, root_ui_path, currentUserEmail):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.currentUserEmail = currentUserEmail
        self.ui = uic.loadUi(self.root_ui_path + "home.ui", self)
        self.setWindowTitle("Home")

        # load data for ui
        self.load_motor_list()
        # event for search button
        self.search_btn.clicked.connect(self.search)
        # Connect the itemClicked signal to the on_item_clicked method
        self.danhsachxe.itemClicked.connect(self.on_item_clicked)

    def load_current_motor(self, id):
        motorController = MotorController()
        motor = motorController.search_by_id(id)
        # change data in widget
        self.ten.setText(motor.get_name())
        self.nam.setText(str(motor.get_publish_year()))
        self.loai.setText(motor.get_motor_type())
        pixmap = QPixmap(motor.get_img())
        self.hinh.setPixmap(pixmap)

    def load_motor_list(self):
        # only show name of motor in list widget
        motorController = MotorController()
        motor_list = motorController.get_all_motors()
        self.load_current_motor(motor_list[0].get_id())
        for motor in motor_list:
            item = QListWidgetItem(
                f"{motor.get_id()}: {motor.get_name()}"
            )  # Create a QListWidgetItem
            self.danhsachxe.addItem(item)

    # bat su kien khi bam chuyen 1 item
    def on_item_clicked(self, item):
        motor_id = item.text().split(":")[0]
        try:
            self.load_current_motor(motor_id)
        except Exception as e:
            print(e)

    def search(self):
        pass
