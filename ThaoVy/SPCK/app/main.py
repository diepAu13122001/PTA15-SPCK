import sys
from PyQt6.QtWidgets import QApplication
from views.login import Login
from views.home import Home

if __name__ == "__main__":
    root_ui_path = "SPCK/app/ui/"
    app = QApplication(sys.argv)
    login_window = Login(root_ui_path)
    login_window.show()
    sys.exit(app.exec())
