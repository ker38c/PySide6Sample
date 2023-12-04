# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Addition.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_left_value = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_left_value.setObjectName(u"lineEdit_left_value")

        self.horizontalLayout.addWidget(self.lineEdit_left_value)

        self.label_add = QLabel(self.verticalLayoutWidget)
        self.label_add.setObjectName(u"label_add")

        self.horizontalLayout.addWidget(self.label_add)

        self.lineEdit_right_value = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_right_value.setObjectName(u"lineEdit_right_value")

        self.horizontalLayout.addWidget(self.lineEdit_right_value)

        self.label_equal = QLabel(self.verticalLayoutWidget)
        self.label_equal.setObjectName(u"label_equal")

        self.horizontalLayout.addWidget(self.label_equal)

        self.label_answer = QLabel(self.verticalLayoutWidget)
        self.label_answer.setObjectName(u"label_answer")

        self.horizontalLayout.addWidget(self.label_answer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button_add = QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName(u"button_add")

        self.verticalLayout.addWidget(self.button_add)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_answer.setText("")
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u7b97", None))
    # retranslateUi

