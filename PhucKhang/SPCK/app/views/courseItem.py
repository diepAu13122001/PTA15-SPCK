from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from controllers.course_controller import CourseController
from models.course import Course


class CourseItem(QWidget):
    def __init__(self, root_ui_path, course: Course, currentUserEmail):
        super().__init__()
        self.courseController = CourseController()
        self.ui = uic.loadUi(root_ui_path + "course.ui", self)

        # change data for course ui
        try:
            self.name.setText(course.get_name())
            pixmap = QPixmap(course.get_icon())
            self.icon.setPixmap(pixmap)
            # self.icon.setScaledContents(False)  # Ensure the image scales properly
            progress = course.get_user_progress(currentUserEmail)
            print(progress)
            self.progress.setValue(int(progress))
        except Exception as e:
            print(e)
