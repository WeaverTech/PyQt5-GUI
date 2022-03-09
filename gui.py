import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStatusBar,
    QLabel,
    QToolBar,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QGridLayout,
)


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Arm controller')
        self.setCentralWidget(QLabel("JD JD JD Central Widget JD JD JD"))
        self.setFixedSize(1080, 920)
        self._createMenu()
        self._createStatusBar()
        self._createButtonBox()
        self._createToolBar()



    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def _createButtonBox(self):
        layout = QGridLayout()
        layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
        layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
        layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
        layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
        layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
        layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
        layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
        layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
