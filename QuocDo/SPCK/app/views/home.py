from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import QTimer, QTime, Qt
from controllers.history_controller import HistoryController
from models.history import History


# Tạo class để chứa giao diện
class Home(QMainWindow):
    def __init__(self, root_ui_path, currentUserEmail):
        super().__init__()
        # Kết nối giao diện với code
        self.ui = uic.loadUi(root_ui_path + "home.ui", self)
        self.root_ui_path = root_ui_path
        self.currentUserEmail = currentUserEmail
        self.historyController = HistoryController()
        self.timer = QTimer(self)
        self.timer.setInterval(100)

        self.show_best_and_worst()
        # khi moi vao khong hien thi danh sach lich su
        self.history_table.hide()

        # bat su kien cho cac button
        self.setting_btn.clicked.connect(self.show_setting)
        self.history_btn.clicked.connect(self.toggle_history)
        self.about_btn.clicked.connect(self.show_about)
        self.start_btn.clicked.connect(self.start_clock)
        self.stop_btn.clicked.connect(self.stop_clock)

    def show_setting(self):
        print("setting")

    def toggle_history(self):
        # check if table hide -> show
        if not self.history_table.isVisible():
            self.load_history_items()
            self.history_table.show()
        else:
            # check if table show -> hide
            self.history_table.hide()

    def show_about(self):
        from views.about import About

        try:
            if not hasattr(self, "about"):
                about = About(self.root_ui_path)
                about.show()
        except Exception as e:
            print(e)

    def start_clock(self):

        try:
            # doi mau button start de biet dang chay
            # xoa du lieu cu
            self.sec.setText("0")
            self.msec.setText("0")
            self.start_btn.setStyleSheet("background-color: green;")
            self.timer.timeout.connect(self.update_time)
            self.timer.start()
            self.update_time()
            self.start_btn.setEnabled(False)
        except Exception as e:
            print(e)

    def update_time(self):
        old_time = int(self.msec.text())
        new_time = old_time + 1
        sec_text = str(new_time // 10 + int(self.sec.text()))
        msec_text = str(new_time % 10)
        self.msec.setText(msec_text)
        self.sec.setText(sec_text)

    def stop_clock(self):
        try:
            self.start_btn.setStyleSheet("background-color: #012a4a;")
            self.start_btn.setEnabled(True)
            self.timer.stop()
            # add du lieu moi vao danh sach
            finish_time = f"{self.sec.text()}.{self.msec.text()}"
            new_history = History(
                0, finish_time, self.currentUserEmail, self.type_cb.currentText()
            )
            self.historyController.add_history(new_history)
            # reset best, worst, list history
            self.load_history_items()
            self.show_best_and_worst()
        except Exception as e:
            print(e)

    def show_best_and_worst(self):
        self.best.setText(
            f"Best: {self.historyController.find_best(self.currentUserEmail)}"
        )
        self.worst.setText(
            f"Worst: {self.historyController.find_worst(self.currentUserEmail)}"
        )

    def load_history_items(self):
        try:
            history_list = self.historyController.search_by_creator(
                self.currentUserEmail
            )
            if history_list:
                # neu co danh sach thi moi load, khong thi bo trong
                self.history_table.setRowCount(
                    len(history_list)
                )  # set do dai cho bang moi dung duoc
                for index, item in enumerate(history_list):
                    self.history_table.setItem(
                        index, 0, QTableWidgetItem(item.get_time())
                    )
                    self.history_table.setItem(
                        index, 1, QTableWidgetItem(item.get_type())
                    )
        except Exception as e:
            print(e)
