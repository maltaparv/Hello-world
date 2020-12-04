import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor


# https://evileg.com/ru/post/579/
# + something renamed...

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 408)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "--- Пример ---"))
        self.pushButton.setText(_translate("MainWindow", "-- ВВОД --"))


# Объект, который будет перенесён в другой поток для выполнения кода
class BrowserHandler(QtCore.QObject):
    # running = False
    newTextAndColor = QtCore.pyqtSignal(str, object)

    # метод, который будет выполнять алгоритм в другом потоке
    def run(self):
        while True:
            # посылаем сигнал из второго потока в GUI поток
            self.newTextAndColor.emit(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - thread 2 var 1.\n', QColor(0, 0, 150))
            QtCore.QThread.msleep(1000)

            # посылаем сигнал из второго потока в GUI поток
            self.newTextAndColor.emit(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - thread 2 var 2.\n', QColor(150, 0, 0))
            QtCore.QThread.msleep(1000)

#class MyWindow():
class MyWindow(QtWidgets.QWidget):
#class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # используем кнопку для добавления текста с цветом в главном потоке
        self.ui.pushButton.clicked.connect(self.addAnotherTextAndColor)

        # создадим поток
        self.thread = QtCore.QThread()
        # создадим объект для выполнения кода в другом потоке
        self.browserHandler = BrowserHandler()
        # перенесём объект в другой поток
        self.browserHandler.moveToThread(self.thread)
        # после чего подключим все сигналы и слоты
        self.browserHandler.newTextAndColor.connect(self.addNewTextAndColor)
        # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
        self.thread.started.connect(self.browserHandler.run)
        # запустим поток
        self.thread.start()

    @QtCore.pyqtSlot(str, object)
    def addNewTextAndColor(self, string, color):
        self.ui.textBrowser.setTextColor(color)
        self.ui.textBrowser.append(string)

    def addAnotherTextAndColor(self):
        self.ui.textBrowser.setTextColor(QColor(0, 200, 0))
        self.ui.textBrowser.append(f'Нажата кл.{time.strftime("%Y-%m-%d %H:%M:%S")} - thread 2 var 3.\n')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

