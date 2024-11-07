import sys
import os
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt
from controllers.course_controller import CourseController
from views.courseItem import CourseItem


class Home(QMainWindow):
    def __init__(self, root_ui_path, currentUserEmail):
        super().__init__()
        self.root_ui_path = root_ui_path
        self.currentUserEmail = currentUserEmail
        self.courseController = CourseController()
        self.ui = uic.loadUi(self.root_ui_path + "home.ui", self)
        self.setWindowTitle("Home")

        # load data for ui
        self.load_courses(3)
        # event for search button
        self.search_btn.clicked.connect(self.search)

    def change_matrix_list(self, list, row_size):
        return [list[i : i + row_size] for i in range(0, len(list), row_size)]

    def load_courses(self, row_size):
        # Clear old data
        try:
            course_list = self.courseController.get_all_courses()
            course_list = self.change_matrix_list(course_list, row_size)
            print(type(course_list))
            # Load new courses
            for row in range(len(course_list)):
                for col in range(min(len(course_list[row]), row_size)):
                    course = course_list[row][col]
                    course_widget = CourseItem(
                        root_ui_path=self.root_ui_path,
                        course=course,
                        currentUserEmail=self.currentUserEmail,
                    )
                    self.course_list.layout().addWidget(course_widget, row, col)

                    # Align the Course widget to the top-left of each cell
                    self.course_list.layout().setAlignment(
                        course_widget,
                        Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
                    )
        except Exception as e:
            print(f"Error loading courses: {e}")

    def search(self):
        pass
