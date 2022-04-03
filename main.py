from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication,
                             QCheckBox,
                             QComboBox,
                             QDateTimeEdit,
                             QDial,
                             QDialog,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QProgressBar,
                             QPushButton,
                             QRadioButton,
                             QScrollBar,
                             QSizePolicy,
                             QSlider,
                             QSpinBox,
                             QStyleFactory,
                             QTableWidget,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget
)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Użyj standardowej palety stylów")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Wyłącz działanie widgetów")
        self.NameText = QLabel("Aplikacje wykonał Maciej Tkacz")

        self.createTopLeftGroupBox()
        self.ControlBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1, 1, 1)
        mainLayout.setRowStretch(1, 2)
        mainLayout.addWidget(self.bottomRightGroupBox, 3, 0, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 3, 1, 3, 2)
        mainLayout.addWidget(self.NameText, 7, 0, 1, 2)
        mainLayout.addWidget(self.progressBar, 6, 0, 1, 2)

        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Style")
        self.changeStyle('Windows')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def button_clicked(self):
        print("klikniete")

    def ControlBox(self):
        self.topRightGroupBox = QGroupBox("Kontrola")

        J1Text = QLabel("Oś 1")
        J1Text.setAlignment(QtCore.Qt.AlignCenter)

        J1PlusButton = QPushButton("+")
        J1PlusButton.clicked.connect(self.button_clicked)

        J1MinusButton = QPushButton("-")
        J1MinusButton.clicked.connect(self.button_clicked)

        J1PlusButton.setDefault(True)
        J1MinusButton.setDefault(True)

        J2Text = QLabel("Oś 2")
        J2Text.setAlignment(QtCore.Qt.AlignCenter)

        J2PlusButton = QPushButton("+")
        J2PlusButton.clicked.connect(self.button_clicked)

        J2MinusButton = QPushButton("-")
        J2MinusButton.clicked.connect(self.button_clicked)


        J2PlusButton.setDefault(True)
        J2MinusButton.setDefault(True)

        layout = QGridLayout()
        layout.addWidget(J1Text, 0, 0, 1, 2)
        layout.addWidget(J1PlusButton, 1, 0)
        layout.addWidget(J1MinusButton, 1, 1)
        layout.addWidget(J2Text, 2, 0, 1, 2)
        layout.addWidget(J2PlusButton, 3, 0)
        layout.addWidget(J2MinusButton, 3, 1)

        self.topRightGroupBox.setLayout(layout)




    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)




    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) // 100)




    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Grupa 1")

        radioButton1 = QRadioButton("Opcja 1")
        radioButton2 = QRadioButton("Opcja 2")
        radioButton3 = QRadioButton("Opcja 3")
        radioButton4 = QRadioButton("Opcja 4")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Zaznacz")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(radioButton4)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)



    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Lorem ipsum dolor sit amet, \n"
                              "consectetur adipiscing elit, \n"
                              "sed do eiusmod tempor incididunt ut \n"
                              "labore et dolore magna aliqua. \n"
                              "Ut enim ad minim veniam, \n"
                              "quis nostrud exercitation ullamco \n"
                              "laboris nisi ut aliquip ex\n"
                              "ea commodo consequat.")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Tabela")
        self.bottomLeftTabWidget.addTab(tab2, "Edytor &Tekstu")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Grupa 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('sekret')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())