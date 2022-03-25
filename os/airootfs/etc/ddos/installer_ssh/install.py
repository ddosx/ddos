from PyQt5 import QtCore, QtGui, QtWidgets
import os,time
class Ui_MainWindow(object):
    def installssh(self,port,host,user):
        if os.path.exists(f'{os.getenv("HOME")}/.ssh/id_rsa'):
            pass
        else:
            os.system(f'konsole -e ssh-keygen') #  -t dsa -N "ssh key" -C "ssh key" -f ~/.ssh/id_rsa

        for i in range(0,31,1):
            time.sleep(0.01)
            self.installbar.setProperty("value", i)
        
        os.system("konsole -e ssh-copy-id "+'"'+f"{user()}@{host()} -p {port()}" + '"')

        for i in range(30,101,1):
            time.sleep(0.01)
            self.installbar.setProperty("value", i)
        MainWindow.hide()
        os.system(f"konsole -e ssh -x {user()}@{host()} -p {port()} "+'"sudo archinstall"')
        MainWindow.show()
        self.installbar.setProperty("value", 0)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 283)
        icon = QtGui.QIcon.fromTheme("debian-installer-launcher")
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.install = QtWidgets.QPushButton(self.centralwidget)
        self.install.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.install.setObjectName("install")
        self.horizontalLayout_2.addWidget(self.install)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setMinimumSize(QtCore.QSize(115, 0))
        self.user.setMaximumSize(QtCore.QSize(115, 16777215))
        self.user.setObjectName("user")
        self.horizontalLayout.addWidget(self.user)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.host = QtWidgets.QLineEdit(self.centralwidget)
        self.host.setMinimumSize(QtCore.QSize(115, 0))
        self.host.setMaximumSize(QtCore.QSize(115, 16777215))
        self.host.setObjectName("host")
        self.horizontalLayout.addWidget(self.host)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.port = QtWidgets.QLineEdit(self.centralwidget)
        self.port.setMinimumSize(QtCore.QSize(35, 0))
        self.port.setMaximumSize(QtCore.QSize(35, 16777215))
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.installbar = QtWidgets.QProgressBar(self.centralwidget)
        self.installbar.setProperty("value", 0)
        self.installbar.setObjectName("installbar")
        self.verticalLayout.addWidget(self.installbar)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.connectUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.user, self.host)
        MainWindow.setTabOrder(self.host, self.port)
        MainWindow.setTabOrder(self.port, self.install)
    def connectUi(self, MainWindow):
        port=self.port.text
        host=self.host.text
        user=self.user.text
        self.install.clicked.connect(lambda: self.installssh(
            host=host,port=port,user=user
        ))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.installbar.setFormat(_translate("MainWindow", "%p%"))
        self.label_2.setText(_translate("MainWindow", "ssh "))
        self.user.setText(_translate("MainWindow", "user"))
        self.label_3.setText(_translate("MainWindow", "@"))
        self.host.setText(_translate("MainWindow", "host"))
        self.label_4.setText(_translate("MainWindow", " -p "))
        self.port.setText(_translate("MainWindow", "22"))


        MainWindow.setWindowTitle(_translate("MainWindow", "Установка ddOSX по ssh"))
        self.install.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow", "Установка ddOSX по ssh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
