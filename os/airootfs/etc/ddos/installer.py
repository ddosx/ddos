from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import time
import os
import sys
import tkinter.messagebox as tkm
args = sys.argv[1:]
if '--mem' in args:
    memest = True
else:
    memest = False
plasma_pkgs = ['plasma-meta','kate']
gnome_pkgs = ['gnome','gnome-extra','gnome-games','gnome-contol-center','gedit']
xfce_pkgs = ['xfce4','xfce4-goodies']
cinnamon_pkgs = ['cinnamon']

lang = 'Russian'
gui = 'plasma'
ldm = 'sddm'
mount = '/mnt'
user = 'dydouser'
hostname = 'dydoblock'
timeregion = 'Europe/Moscow'
libreoffice = False
konsole = True
firefox = True
pamac = True
yay = True
archrepo = True
kernel = 'linux-zen'
bootloader = 'refind'
gpudriver = 'xf86-video-ati xf86-video-amdgpu xf86-video-intel mesa'


class Ui_MainWindow(object):
    def add_func(self):
        self.pushButton.clicked.connect(self.startinstaller)
        self.dalee_button.clicked.connect(self.nextstep2)
        self.dalee_button_3.clicked.connect(self.startinstallation)
        
        self.complete.clicked.connect(self.close)
    def close():
        sys.exit(app.exec_())
    def startinstaller(self):
        # self.a_welcome_screen.setGeometry(QtCore.QRect(25, -6100, 550, 350))
        # self.aa_settings_screen.setGeometry(QtCore.QRect(25, 100, 550, 361))

        self.animation1 = Qt.QPropertyAnimation(self.a_welcome_screen, b"geometry")
        self.animation1.setDuration(100)
        self.animation1.setStartValue(Qt.QRect(25, 100, 550, 350))
        self.animation1.setEndValue(Qt.QRect(-550, 100, 550, 350))
        self.animation2 = Qt.QPropertyAnimation(self.aa_settings_screen, b"geometry")
        self.animation2.setDuration(100)
        self.animation2.setStartValue(Qt.QRect(700, 100, 550, 350))
        self.animation2.setEndValue(Qt.QRect(25, 100, 550, 350))


        self.animation1.start()
        self.animation2.start()
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", i//10)
        
    
    def nextstep2(self):
        self.animation3 = Qt.QPropertyAnimation(self.aa_settings_screen, b"geometry")
        self.animation3.setDuration(100)
        self.animation3.setStartValue(Qt.QRect(25, 100, 550, 350))
        self.animation3.setEndValue(Qt.QRect(-550, 100, 550, 350))
        self.animation4 = Qt.QPropertyAnimation(self.aaa_settings_screen, b"geometry")
        self.animation4.setDuration(100)
        self.animation4.setStartValue(Qt.QRect(650, 100, 550, 350))
        self.animation4.setEndValue(Qt.QRect(25, 100, 550, 350))


        self.animation3.start()
        self.animation4.start()
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+10)

    def startinstallation(self):
        tkm.showinfo('Предупреждение',"Подмонтируйте все ДИСКИ в {}".format(self.path.text()))
        # de
        if self.gnomede.isChecked():
            de = 'gnome'
        if self.kdede.isChecked():
            de = 'plasma'
        if self.cinnamonde.isChecked():
            de = 'cinnamon'
        if self.xfcede.isChecked():
            de = 'xfce4'
        # lde
        if self.sddm.isChecked():
            lde = 'sddm'
        if self.lightdm.isChecked():
            lde = 'lightdm'
        if self.gdm.isChecked():
            lde = 'gdm'
        # kernel
        if self.linuxclear.isChecked():
            kernel = 'linux-clear'
        if self.linuxlqx.isChecked():
            kernel = 'linux-lqx'
        if self.linuxzen.isChecked():
            kernel = 'linux-zen'
        if self.linuxnvidia.isChecked():
            kernel = 'linux'
        # gpudriver
        if self.videoamdati.isChecked():
            gpudriver = 'xf86-video-amdgpu xf86-video-ati'
            gpud = 'atiamd'
        if self.videointel.isChecked():
            gpudriver = 'xf86-video-intel'
            gpud = 'intel'
        if self.videonoveau.isChecked():
            gpudriver = 'mesa'
            gpud = 'mesa'
        if self.videonvide.isChecked():
            gpudriver = 'nvidia nvidia-utils'
            gpud = 'nvd'
        if self.videoopen.isChecked():
            gpudriver = 'xf86-video-amdgpu xf86-video-ati xf86-video-intel mesa'
            gpud = 'open'
        # bootloader
        if self.refind.isChecked():
            bootloader = 'refind'
        if self.grub2.isChecked():
            bootloader = 'grub2'
        if self.grub2bios.isChecked():
            bootloader = 'grub2bios'
        # mount
        mountX = self.path.text()
        # hostname
        hostnameX = self.hostname.text()
        # timeregion
        timedateX = self.timedate.text()
        # user
        userX = self.user.text()
        # apps
        yay = (self.yay.checkState() == 2)
        pamac = (self.pamac.checkState() == 2)
        archrepo = (self.archrepo.checkState() == 2)
        libreoffice = (self.libreoffice.checkState() == 2)
        firefox = (self.firefox.checkState() == 2)
        konsole = (self.konsole.checkState() == 2)
        # to installtion
        os.system('echo "installationdata {">install.txt')
        os.system('echo "   kernel: ::::'+str(kernel)+'::::">>install.txt')
        os.system('echo "   bootloader: ::::'+str(bootloader)+'::::">>install.txt')
        os.system('echo "   gpudrivers: ::::'+str(gpudriver)+'::::">>install.txt')
        os.system('echo "   de: ::::'+str(de)+'::::">>install.txt')
        os.system('echo "   lde: ::::'+str(lde)+'::::">>install.txt')
        os.system('echo "   mount: ::::'+str(mountX)+'::::">>install.txt')
        os.system('echo "   hostname: ::::'+str(hostnameX)+'::::">>install.txt')
        os.system('echo "   timedate: ::::'+str(timedateX)+'::::">>install.txt')
        os.system('echo "   user: ::::'+str(userX)+'::::">>install.txt')
        os.system('echo "   firefox: ::::'+str(firefox)+'::::">>install.txt')
        os.system('echo "   konsole: ::::'+str(konsole)+'::::">>install.txt')
        os.system('echo "   pamac: ::::'+str(pamac)+'::::">>install.txt')
        os.system('echo "   yay: ::::'+str(yay)+'::::">>install.txt')
        os.system('echo "   archrepo: ::::'+str(archrepo)+'::::">>install.txt')
        os.system('echo "   libreoffice: ::::'+str(libreoffice)+'::::">>install.txt')
        os.system('echo "}">>install.txt')

        self.animation5 = Qt.QPropertyAnimation(self.aaa_settings_screen, b"geometry")
        self.animation5.setDuration(100)
        self.animation5.setStartValue(Qt.QRect(25, 100, 550, 350))
        self.animation5.setEndValue(Qt.QRect(-550, 100, 550, 350))
        self.animation6 = Qt.QPropertyAnimation(self.aaaa_installing_screen, b"geometry")
        self.animation6.setDuration(100)
        self.animation6.setStartValue(Qt.QRect(700, 100, 550, 350))
        self.animation6.setEndValue(Qt.QRect(25, 100, 550, 350))


        self.animation5.start()
        self.animation6.start()

        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+20)

        self.aaa_settings_screen.setGeometry(QtCore.QRect(25, -600, 550, 361))
        self.aaaa_installing_screen.setGeometry(QtCore.QRect(25, 100, 550, 361))
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+30)

        os.system(
            "konsole -e python /etc/ddos/installer/installers/install_base.py {} {} {} {} {} {} {}".format(
                kernel,bootloader,self.path.text(),self.hostname.text(),self.timedate.text(),self.user.text(),archrepo
                ))
        # print('installing os :::: complete')

        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+40)

        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+50)

        os.system(
            "konsole -e python /etc/ddos/installer/installers/install_gui.py {} {} {} {} {}".format(
                de,lde,gpud,mountX,archrepo
            )
        )
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+60)
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+70)
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+80)
        print('installing gui :::: complete')
        os.system("konsole -e python /etc/ddos/installer/installers/install_add.py {} {} {} {} {} {} {} {}".format(firefox,konsole,pamac,yay,libreoffice,mountX,archrepo,de))
        for i in range(101):
            time.sleep(0.001)
            self.installing_bar.setProperty("value", (i//10)+90)
        # print('installing add :::: complete')
        self.installation_complete()


    def installation_complete(self):
        # self.aaaa_installing_screen.setGeometry(QtCore.QRect(25, -6100, 550, 350))
        # self.aaaaa_complete_screen.setGeometry(QtCore.QRect(25, 100, 550, 361))

        self.animation7 = Qt.QPropertyAnimation(self.aaaa_installing_screen, b"geometry")
        self.animation7.setDuration(100)
        self.animation7.setStartValue(Qt.QRect(25, 100, 550, 350))
        self.animation7.setEndValue(Qt.QRect(-550, 100, 550, 350))
        self.animation8 = Qt.QPropertyAnimation(self.aaaaa_complete_screen, b"geometry")
        self.animation8.setDuration(100)
        self.animation8.setStartValue(Qt.QRect(700, 100, 550, 350))
        self.animation8.setEndValue(Qt.QRect(25, 100, 550, 350))
        self.animation7.start()
        self.animation8.start()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.window = QtWidgets.QWidget(MainWindow)
        self.window.setObjectName("window")
        self.installing_bar = QtWidgets.QProgressBar(self.window)
        self.installing_bar.setGeometry(QtCore.QRect(0, 0, 600, 50))
        self.installing_bar.setProperty("value", 0)
        self.installing_bar.setObjectName("installing_bar")
        self.installing_info1 = QtWidgets.QLabel(self.window)
        self.installing_info1.setGeometry(QtCore.QRect(0, 50, 131, 25))
        self.installing_info1.setObjectName("installing_info1")
        self.installing_info2 = QtWidgets.QLabel(self.window)
        self.installing_info2.setGeometry(QtCore.QRect(120, 50, 131, 25))
        self.installing_info2.setObjectName("installing_info2")
        self.a_welcome_screen = QtWidgets.QWidget(self.window)
        self.a_welcome_screen.setGeometry(QtCore.QRect(25, 100, 550, 350))
        font = QtGui.QFont()
        font.setFamily("Google Sans Medium")
        self.a_welcome_screen.setFont(font)
        self.a_welcome_screen.setObjectName("a_welcome_screen")
        self.label = QtWidgets.QLabel(self.a_welcome_screen)
        self.label.setGeometry(QtCore.QRect(0, 130, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.a_welcome_screen)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.aa_settings_screen = QtWidgets.QWidget(self.window)
        self.aa_settings_screen.setEnabled(True)
        self.aa_settings_screen.setGeometry(QtCore.QRect(600, 100, 550, 361))
        self.aa_settings_screen.setStyleSheet("")
        self.aa_settings_screen.setObjectName("aa_settings_screen")
        self.path = QtWidgets.QLineEdit(self.aa_settings_screen)
        self.path.setGeometry(QtCore.QRect(30, 190, 110, 25))
        self.path.setObjectName("path")
        self.de = QtWidgets.QWidget(self.aa_settings_screen)
        self.de.setGeometry(QtCore.QRect(30, 40, 150, 110))
        self.de.setObjectName("de")
        self.gnomede = QtWidgets.QRadioButton(self.de)
        self.gnomede.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.gnomede.setObjectName("gnomede")
        # layout.addWidget(de, 0, 0)
        self.kdede = QtWidgets.QRadioButton(self.de)
        self.kdede.setGeometry(QtCore.QRect(0, 25, 150, 30))
        self.kdede.setObjectName("kdede")
        self.cinnamonde = QtWidgets.QRadioButton(self.de)
        self.cinnamonde.setGeometry(QtCore.QRect(0, 55, 150, 30))
        self.cinnamonde.setObjectName("cinnamonde")
        self.xfcede = QtWidgets.QRadioButton(self.de)
        self.xfcede.setGeometry(QtCore.QRect(0, 80, 150, 30))
        self.xfcede.setObjectName("xfcede")
        self.user = QtWidgets.QLineEdit(self.aa_settings_screen)
        self.user.setGeometry(QtCore.QRect(30, 260, 110, 25))
        self.user.setObjectName("user")
        self.label_2 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_3.setGeometry(QtCore.QRect(0, 150, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_4.setGeometry(QtCore.QRect(0, 220, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_5.setGeometry(QtCore.QRect(0, 300, 111, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.hostname = QtWidgets.QLineEdit(self.aa_settings_screen)
        self.hostname.setGeometry(QtCore.QRect(110, 310, 110, 25))
        self.hostname.setObjectName("hostname")
        self.label_6 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_6.setGeometry(QtCore.QRect(280, 150, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.timedate = QtWidgets.QLineEdit(self.aa_settings_screen)
        self.timedate.setGeometry(QtCore.QRect(310, 190, 151, 25))
        self.timedate.setObjectName("timedate")
        self.lde = QtWidgets.QWidget(self.aa_settings_screen)
        self.lde.setGeometry(QtCore.QRect(310, 40, 150, 110))
        self.lde.setObjectName("lde")
        self.gdm = QtWidgets.QRadioButton(self.lde)
        self.gdm.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.gdm.setObjectName("gdm")
        self.sddm = QtWidgets.QRadioButton(self.lde)
        self.sddm.setGeometry(QtCore.QRect(0, 25, 150, 30))
        self.sddm.setObjectName("sddm")
        self.lightdm = QtWidgets.QRadioButton(self.lde)
        self.lightdm.setGeometry(QtCore.QRect(0, 55, 150, 30))
        self.lightdm.setObjectName("lightdm")
        self.label_7 = QtWidgets.QLabel(self.aa_settings_screen)
        self.label_7.setGeometry(QtCore.QRect(280, 0, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.libreoffice = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.libreoffice.setGeometry(QtCore.QRect(280, 230, 86, 27))
        self.libreoffice.setObjectName("libreoffice")
        self.firefox = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.firefox.setGeometry(QtCore.QRect(280, 260, 86, 27))
        self.firefox.setChecked(True)
        self.firefox.setObjectName("firefox")
        self.konsole = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.konsole.setGeometry(QtCore.QRect(280, 290, 86, 27))
        self.konsole.setChecked(True)
        self.konsole.setObjectName("konsole")
        self.pamac = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.pamac.setGeometry(QtCore.QRect(380, 230, 86, 27))
        self.pamac.setChecked(True)
        self.pamac.setObjectName("pamac")
        self.yay = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.yay.setGeometry(QtCore.QRect(380, 260, 86, 27))
        self.yay.setChecked(True)
        self.yay.setObjectName("yay")
        self.archrepo = QtWidgets.QCheckBox(self.aa_settings_screen)
        self.archrepo.setGeometry(QtCore.QRect(380, 290, 86, 27))
        self.archrepo.setChecked(True)
        self.archrepo.setObjectName("archrepo")
        self.dalee_button = QtWidgets.QPushButton(self.aa_settings_screen)
        self.dalee_button.setGeometry(QtCore.QRect(450, 320, 92, 37))
        self.dalee_button.setObjectName("dalee_button")
        self.aaaa_installing_screen = QtWidgets.QWidget(self.window)
        self.aaaa_installing_screen.setGeometry(QtCore.QRect(25, -6100, 550, 350))
        self.aaaa_installing_screen.setObjectName("aaaa_installing_screen")
        self.label_9 = QtWidgets.QLabel(self.aaaa_installing_screen)
        self.label_9.setGeometry(QtCore.QRect(0, 150, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        # self.reboot_after_installing = QtWidgets.QCheckBox(self.aaaa_installing_screen)
        # self.reboot_after_installing.setGeometry(QtCore.QRect(10, 190, 231, 27))
        # self.reboot_after_installing.setObjectName("reboot_after_installing")
        self.aaaaa_complete_screen = QtWidgets.QWidget(self.window)
        self.aaaaa_complete_screen.setGeometry(QtCore.QRect(25, -6100, 550, 350))
        self.aaaaa_complete_screen.setObjectName("aaaaa_complete_screen")
        self.label_10 = QtWidgets.QLabel(self.aaaaa_complete_screen)
        self.label_10.setGeometry(QtCore.QRect(0, 150, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        # self.reboot = QtWidgets.QCheckBox(self.aaaaa_complete_screen)
        # self.reboot.setGeometry(QtCore.QRect(10, 190, 121, 27))
        # self.reboot.setObjectName("reboot")
        self.complete = QtWidgets.QPushButton(self.aaaaa_complete_screen)
        self.complete.setGeometry(QtCore.QRect(430, 300, 92, 37))
        self.complete.setObjectName("complete")
        self.aaa_settings_screen = QtWidgets.QWidget(self.window)
        self.aaa_settings_screen.setEnabled(True)
        self.aaa_settings_screen.setGeometry(QtCore.QRect(1200, 100, 550, 361))
        self.aaa_settings_screen.setStyleSheet("")
        self.aaa_settings_screen.setObjectName("aaa_settings_screen")
        self.kernel = QtWidgets.QWidget(self.aaa_settings_screen)
        self.kernel.setGeometry(QtCore.QRect(30, 40, 150, 110))
        self.kernel.setObjectName("kernel")
        self.linuxzen = QtWidgets.QRadioButton(self.kernel)
        self.linuxzen.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.linuxzen.setObjectName("linuxzen")
        self.linuxlqx = QtWidgets.QRadioButton(self.kernel)
        self.linuxlqx.setGeometry(QtCore.QRect(0, 25, 150, 30))
        self.linuxlqx.setChecked(True)
        self.linuxlqx.setObjectName("linuxlqx")
        self.linuxclear = QtWidgets.QRadioButton(self.kernel)
        self.linuxclear.setGeometry(QtCore.QRect(0, 55, 150, 30))
        self.linuxclear.setObjectName("linuxclear")
        self.linuxnvidia = QtWidgets.QRadioButton(self.kernel)
        self.linuxnvidia.setGeometry(QtCore.QRect(0, 80, 150, 30))
        self.linuxnvidia.setObjectName("linuxnvidia")
        self.label_16 = QtWidgets.QLabel(self.aaa_settings_screen)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gpu_driver = QtWidgets.QWidget(self.aaa_settings_screen)
        self.gpu_driver.setGeometry(QtCore.QRect(310, 40, 150, 141))
        self.gpu_driver.setObjectName("gpu_driver")
        self.videointel = QtWidgets.QRadioButton(self.gpu_driver)
        self.videointel.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.videointel.setObjectName("videointel")
        self.videoamdati = QtWidgets.QRadioButton(self.gpu_driver)
        self.videoamdati.setGeometry(QtCore.QRect(0, 25, 150, 30))
        self.videoamdati.setObjectName("videoamdati")
        self.videonoveau = QtWidgets.QRadioButton(self.gpu_driver)
        self.videonoveau.setGeometry(QtCore.QRect(0, 55, 150, 30))
        self.videonoveau.setObjectName("videonoveau")
        self.videonvide = QtWidgets.QRadioButton(self.gpu_driver)
        self.videonvide.setGeometry(QtCore.QRect(0, 80, 150, 30))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.videonvide.setFont(font)
        self.videonvide.setStyleSheet("color: rgb(255, 0, 4);")
        self.videonvide.setObjectName("videonvide")
        self.videoopen = QtWidgets.QRadioButton(self.gpu_driver)
        self.videoopen.setGeometry(QtCore.QRect(0, 110, 150, 30))
        self.videoopen.setStyleSheet("color: rgb(255, 0, 4);")
        self.videoopen.setChecked(True)
        self.videoopen.setObjectName("videoopen")
        self.label_21 = QtWidgets.QLabel(self.aaa_settings_screen)
        self.label_21.setGeometry(QtCore.QRect(280, 0, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.dalee_button_3 = QtWidgets.QPushButton(self.aaa_settings_screen)
        self.dalee_button_3.setGeometry(QtCore.QRect(450, 320, 92, 37))
        self.dalee_button_3.setObjectName("dalee_button_3")
        self.label_17 = QtWidgets.QLabel(self.aaa_settings_screen)
        self.label_17.setGeometry(QtCore.QRect(0, 180, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.boolloader = QtWidgets.QWidget(self.aaa_settings_screen)
        self.boolloader.setGeometry(QtCore.QRect(30, 220, 150, 110))
        self.boolloader.setObjectName("boolloader")
        self.grub2 = QtWidgets.QRadioButton(self.boolloader)
        self.grub2.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.grub2.setObjectName("grub2")
        self.refind = QtWidgets.QRadioButton(self.boolloader)
        self.refind.setGeometry(QtCore.QRect(0, 25, 150, 30))
        self.refind.setChecked(True)
        self.refind.setObjectName("refind")
        self.grub2bios = QtWidgets.QRadioButton(self.boolloader)
        self.grub2bios.setGeometry(QtCore.QRect(0, 55, 150, 30))
        self.grub2bios.setObjectName("grub2bios")
        MainWindow.setCentralWidget(self.window)
        self.kdede.setChecked(True)
        self.sddm.setChecked(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 
        
        self.installing_info1.setText(_translate("MainWindow", "Сбор информации"))
        self.installing_info2.setText(_translate("MainWindow", "Установка"))
        if memest ==False:
            self.label.setText(_translate("MainWindow", "Добро пожаловать в установщик ddos"))
            self.label_2.setText(_translate("MainWindow", "Оболочка рабочего стола"))
            self.label_7.setText(_translate("MainWindow", "Экран входа в OC"))
            self.label_17.setText(_translate("MainWindow", "Загрузчик"))
            MainWindow.setWindowTitle(_translate("MainWindow", "Installer"))
        else:
            self.label.setText(_translate("MainWindow", "Добро пожаловать в инсталер ddos"))
            self.label_2.setText(_translate("MainWindow", "Морда ОСИ"))
            self.label_7.setText(_translate("MainWindow", "Морда ВХОДА в ОСЬ"))
            self.label_17.setText(_translate("MainWindow", "Лоадер"))
            MainWindow.setWindowTitle(_translate("MainWindow", "Ну типо инсталер"))
        self.pushButton.setText(_translate("MainWindow", "Установить"))
        
        self.path.setText(_translate("MainWindow", "/mnt"))
        self.gnomede.setText(_translate("MainWindow", "gnome"))
        self.kdede.setText(_translate("MainWindow", "kde"))
        self.cinnamonde.setText(_translate("MainWindow", "cinnamon"))
        self.xfcede.setText(_translate("MainWindow", "xfce"))
        self.user.setText(_translate("MainWindow", "user"))
        # 
        
        self.label_3.setText(_translate("MainWindow", "Точка монтирования дисков"))
        self.label_4.setText(_translate("MainWindow", "Пользователь"))
        self.label_5.setText(_translate("MainWindow", "Имя хоста :"))
        self.hostname.setText(_translate("MainWindow", "ddos_pc"))
        self.label_6.setText(_translate("MainWindow", "Регион времени"))
        self.timedate.setText(_translate("MainWindow", "Europe/Moscow"))
        self.gdm.setText(_translate("MainWindow", "gdm"))
        self.sddm.setText(_translate("MainWindow", "sddm"))
        self.lightdm.setText(_translate("MainWindow", "lightdm"))
        # 
        
        self.libreoffice.setText(_translate("MainWindow", "libreoffice"))
        self.firefox.setText(_translate("MainWindow", "firefox"))
        self.konsole.setText(_translate("MainWindow", "konsole"))
        self.pamac.setText(_translate("MainWindow", "pamac"))
        self.yay.setText(_translate("MainWindow", "yay"))
        self.archrepo.setText(_translate("MainWindow", "archrepo"))
        self.dalee_button.setText(_translate("MainWindow", "Далее"))
        self.label_9.setText(_translate("MainWindow", "Идёт установка"))
        # self.reboot_after_installing.setText(_translate("MainWindow", "Перезагрузить после установки"))
        self.label_10.setText(_translate("MainWindow", "Система установленна на ваш ПК"))
        # self.reboot.setText(_translate("MainWindow", "Перезагрузить"))
        self.complete.setText(_translate("MainWindow", "Готово"))
        self.linuxzen.setText(_translate("MainWindow", "linux-zen"))
        self.linuxlqx.setText(_translate("MainWindow", "linux-lqx"))
        self.linuxclear.setText(_translate("MainWindow", "linux-clear zen3"))
        self.linuxnvidia.setText(_translate("MainWindow", "linux (nvidia)"))
        self.label_16.setText(_translate("MainWindow", "Ядро"))
        self.videointel.setText(_translate("MainWindow", "intel IGPU"))
        self.videoamdati.setText(_translate("MainWindow", "amd/ati GPU/iGPU"))
        self.videonoveau.setText(_translate("MainWindow", "nvidia OPEN"))
        self.videonvide.setText(_translate("MainWindow", "NVIDIA (CLOSE)"))
        self.videoopen.setText(_translate("MainWindow", "all opensource"))
        self.label_21.setText(_translate("MainWindow", "Видеодрайвер"))
        self.dalee_button_3.setText(_translate("MainWindow", "Далее"))
        # 
        
        self.grub2.setText(_translate("MainWindow", "grub2"))
        self.refind.setText(_translate("MainWindow", "rEFInd"))
        self.grub2bios.setText(_translate("MainWindow", "grub2 (BIOS)"))
        self.add_func()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
