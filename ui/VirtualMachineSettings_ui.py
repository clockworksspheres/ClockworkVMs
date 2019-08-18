# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/VMSettings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VmSettings_ui(object):
    def setupUi(self, VmSettings_ui):
        VmSettings_ui.setObjectName("VmSettings_ui")
        VmSettings_ui.resize(620, 400)
        self.gridLayout = QtWidgets.QGridLayout(VmSettings_ui)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(VmSettings_ui)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.generalButton = QtWidgets.QPushButton(VmSettings_ui)
        self.generalButton.setObjectName("generalButton")
        self.gridLayout.addWidget(self.generalButton, 1, 0, 1, 1)
        self.isoButton = QtWidgets.QPushButton(VmSettings_ui)
        self.isoButton.setObjectName("isoButton")
        self.gridLayout.addWidget(self.isoButton, 1, 1, 1, 1)
        self.hardwareButton = QtWidgets.QPushButton(VmSettings_ui)
        self.hardwareButton.setObjectName("hardwareButton")
        self.gridLayout.addWidget(self.hardwareButton, 1, 2, 1, 1)
        self.userButton = QtWidgets.QPushButton(VmSettings_ui)
        self.userButton.setObjectName("userButton")
        self.gridLayout.addWidget(self.userButton, 1, 3, 1, 1)
        self.proxiesButton = QtWidgets.QPushButton(VmSettings_ui)
        self.proxiesButton.setObjectName("proxiesButton")
        self.gridLayout.addWidget(self.proxiesButton, 1, 4, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(VmSettings_ui)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.leComment = QtWidgets.QLineEdit(self.page)
        self.leComment.setGeometry(QtCore.QRect(100, 20, 341, 21))
        self.leComment.setObjectName("leComment")
        self.leVmName = QtWidgets.QLineEdit(self.page)
        self.leVmName.setGeometry(QtCore.QRect(100, 60, 341, 21))
        self.leVmName.setObjectName("leVmName")
        self.chkVmware = QtWidgets.QCheckBox(self.page)
        self.chkVmware.setGeometry(QtCore.QRect(20, 100, 86, 20))
        self.chkVmware.setObjectName("chkVmware")
        self.chkVbox = QtWidgets.QCheckBox(self.page)
        self.chkVbox.setGeometry(QtCore.QRect(20, 130, 86, 20))
        self.chkVbox.setObjectName("chkVbox")
        self.chkParallels = QtWidgets.QCheckBox(self.page)
        self.chkParallels.setGeometry(QtCore.QRect(20, 160, 86, 20))
        self.chkParallels.setObjectName("chkParallels")
        self.chkDesktop = QtWidgets.QCheckBox(self.page)
        self.chkDesktop.setGeometry(QtCore.QRect(290, 100, 86, 20))
        self.chkDesktop.setObjectName("chkDesktop")
        self.chkUpdate = QtWidgets.QCheckBox(self.page)
        self.chkUpdate.setGeometry(QtCore.QRect(430, 100, 86, 20))
        self.chkUpdate.setObjectName("chkUpdate")
        self.chkVagrant = QtWidgets.QCheckBox(self.page)
        self.chkVagrant.setGeometry(QtCore.QRect(20, 190, 86, 16))
        self.chkVagrant.setObjectName("chkVagrant")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 59, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 59, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(30, 110, 59, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 131, 16))
        self.label_7.setObjectName("label_7")
        self.leIsoName = QtWidgets.QLineEdit(self.page_3)
        self.leIsoName.setGeometry(QtCore.QRect(100, 20, 411, 21))
        self.leIsoName.setObjectName("leIsoName")
        self.leIsoUrl = QtWidgets.QLineEdit(self.page_3)
        self.leIsoUrl.setGeometry(QtCore.QRect(100, 50, 411, 21))
        self.leIsoUrl.setObjectName("leIsoUrl")
        self.leIsoHash = QtWidgets.QLineEdit(self.page_3)
        self.leIsoHash.setGeometry(QtCore.QRect(100, 110, 411, 21))
        self.leIsoHash.setObjectName("leIsoHash")
        self.leIsoPath = QtWidgets.QLineEdit(self.page_3)
        self.leIsoPath.setGeometry(QtCore.QRect(100, 80, 411, 21))
        self.leIsoPath.setObjectName("leIsoPath")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(30, 80, 59, 16))
        self.label_11.setObjectName("label_11")
        self.leIsoHashAlgorithm = QtWidgets.QLineEdit(self.page_3)
        self.leIsoHashAlgorithm.setGeometry(QtCore.QRect(160, 140, 351, 21))
        self.leIsoHashAlgorithm.setObjectName("leIsoHashAlgorithm")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_10.setObjectName("label_10")
        self.leCpus = QtWidgets.QLineEdit(self.page_4)
        self.leCpus.setGeometry(QtCore.QRect(110, 10, 113, 21))
        self.leCpus.setObjectName("leCpus")
        self.leMemSize = QtWidgets.QLineEdit(self.page_4)
        self.leMemSize.setGeometry(QtCore.QRect(110, 40, 113, 21))
        self.leMemSize.setObjectName("leMemSize")
        self.leDiskSize = QtWidgets.QLineEdit(self.page_4)
        self.leDiskSize.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.leDiskSize.setObjectName("leDiskSize")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.leUserName = QtWidgets.QLineEdit(self.page_5)
        self.leUserName.setGeometry(QtCore.QRect(140, 20, 261, 21))
        self.leUserName.setObjectName("leUserName")
        self.leUserPassword = QtWidgets.QLineEdit(self.page_5)
        self.leUserPassword.setGeometry(QtCore.QRect(140, 50, 261, 21))
        self.leUserPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leUserPassword.setObjectName("leUserPassword")
        self.leVerifyPassword = QtWidgets.QLineEdit(self.page_5)
        self.leVerifyPassword.setGeometry(QtCore.QRect(140, 80, 261, 21))
        self.leVerifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leVerifyPassword.setObjectName("leVerifyPassword")
        self.leUserHomeDir = QtWidgets.QLineEdit(self.page_5)
        self.leUserHomeDir.setGeometry(QtCore.QRect(140, 150, 261, 21))
        self.leUserHomeDir.setObjectName("leUserHomeDir")
        self.leUserShell = QtWidgets.QLineEdit(self.page_5)
        self.leUserShell.setGeometry(QtCore.QRect(140, 180, 261, 21))
        self.leUserShell.setObjectName("leUserShell")
        self.laUserName = QtWidgets.QLabel(self.page_5)
        self.laUserName.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.laUserName.setObjectName("laUserName")
        self.laUserPassword = QtWidgets.QLabel(self.page_5)
        self.laUserPassword.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.laUserPassword.setObjectName("laUserPassword")
        self.laVerifyPassword = QtWidgets.QLabel(self.page_5)
        self.laVerifyPassword.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.laVerifyPassword.setObjectName("laVerifyPassword")
        self.laUserHomeDir = QtWidgets.QLabel(self.page_5)
        self.laUserHomeDir.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.laUserHomeDir.setObjectName("laUserHomeDir")
        self.laUserShell = QtWidgets.QLabel(self.page_5)
        self.laUserShell.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.laUserShell.setObjectName("laUserShell")
        self.laUserComment = QtWidgets.QLabel(self.page_5)
        self.laUserComment.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.laUserComment.setWordWrap(True)
        self.laUserComment.setObjectName("laUserComment")
        self.leUserComment = QtWidgets.QLineEdit(self.page_5)
        self.leUserComment.setGeometry(QtCore.QRect(140, 110, 261, 21))
        self.leUserComment.setObjectName("leUserComment")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.laHttp_proxy = QtWidgets.QLabel(self.page_6)
        self.laHttp_proxy.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.laHttp_proxy.setObjectName("laHttp_proxy")
        self.laHttps_proxy = QtWidgets.QLabel(self.page_6)
        self.laHttps_proxy.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.laHttps_proxy.setObjectName("laHttps_proxy")
        self.laFtpProxy = QtWidgets.QLabel(self.page_6)
        self.laFtpProxy.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.laFtpProxy.setObjectName("laFtpProxy")
        self.laRsyncProxy = QtWidgets.QLabel(self.page_6)
        self.laRsyncProxy.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.laRsyncProxy.setObjectName("laRsyncProxy")
        self.leHttpProxy = QtWidgets.QLineEdit(self.page_6)
        self.leHttpProxy.setGeometry(QtCore.QRect(110, 10, 241, 21))
        self.leHttpProxy.setObjectName("leHttpProxy")
        self.leHttpsProxy = QtWidgets.QLineEdit(self.page_6)
        self.leHttpsProxy.setGeometry(QtCore.QRect(110, 40, 241, 21))
        self.leHttpsProxy.setObjectName("leHttpsProxy")
        self.leFtpProxy = QtWidgets.QLineEdit(self.page_6)
        self.leFtpProxy.setGeometry(QtCore.QRect(110, 70, 241, 21))
        self.leFtpProxy.setObjectName("leFtpProxy")
        self.leRsyncProxy = QtWidgets.QLineEdit(self.page_6)
        self.leRsyncProxy.setGeometry(QtCore.QRect(110, 100, 241, 21))
        self.leRsyncProxy.setObjectName("leRsyncProxy")
        self.laNoProxy = QtWidgets.QLabel(self.page_6)
        self.laNoProxy.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.laNoProxy.setObjectName("laNoProxy")
        self.leNoProxy = QtWidgets.QLineEdit(self.page_6)
        self.leNoProxy.setGeometry(QtCore.QRect(110, 130, 241, 21))
        self.leNoProxy.setObjectName("leNoProxy")
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 5)
        self.buttonBox = QtWidgets.QDialogButtonBox(VmSettings_ui)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 3)

        self.retranslateUi(VmSettings_ui)
        self.stackedWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(VmSettings_ui.accept)
        self.buttonBox.rejected.connect(VmSettings_ui.reject)
        QtCore.QMetaObject.connectSlotsByName(VmSettings_ui)
        VmSettings_ui.setTabOrder(self.generalButton, self.isoButton)
        VmSettings_ui.setTabOrder(self.isoButton, self.hardwareButton)
        VmSettings_ui.setTabOrder(self.hardwareButton, self.userButton)
        VmSettings_ui.setTabOrder(self.userButton, self.proxiesButton)
        VmSettings_ui.setTabOrder(self.proxiesButton, self.leComment)
        VmSettings_ui.setTabOrder(self.leComment, self.leVmName)
        VmSettings_ui.setTabOrder(self.leVmName, self.leIsoName)
        VmSettings_ui.setTabOrder(self.leIsoName, self.leIsoUrl)
        VmSettings_ui.setTabOrder(self.leIsoUrl, self.leIsoHash)
        VmSettings_ui.setTabOrder(self.leIsoHash, self.leCpus)
        VmSettings_ui.setTabOrder(self.leCpus, self.leMemSize)
        VmSettings_ui.setTabOrder(self.leMemSize, self.leDiskSize)
        VmSettings_ui.setTabOrder(self.leDiskSize, self.leUserName)
        VmSettings_ui.setTabOrder(self.leUserName, self.leUserPassword)
        VmSettings_ui.setTabOrder(self.leUserPassword, self.leVerifyPassword)
        VmSettings_ui.setTabOrder(self.leVerifyPassword, self.leUserComment)
        VmSettings_ui.setTabOrder(self.leUserComment, self.leUserHomeDir)
        VmSettings_ui.setTabOrder(self.leUserHomeDir, self.leUserShell)
        VmSettings_ui.setTabOrder(self.leUserShell, self.leHttpProxy)
        VmSettings_ui.setTabOrder(self.leHttpProxy, self.leHttpsProxy)
        VmSettings_ui.setTabOrder(self.leHttpsProxy, self.leFtpProxy)
        VmSettings_ui.setTabOrder(self.leFtpProxy, self.leRsyncProxy)
        VmSettings_ui.setTabOrder(self.leRsyncProxy, self.leNoProxy)

    def retranslateUi(self, VmSettings_ui):
        _translate = QtCore.QCoreApplication.translate
        VmSettings_ui.setWindowTitle(_translate("VmSettings_ui", "Dialog"))
        self.label.setText(_translate("VmSettings_ui", "Virtual Machine Settings"))
        self.generalButton.setText(_translate("VmSettings_ui", "General"))
        self.isoButton.setText(_translate("VmSettings_ui", "ISO"))
        self.hardwareButton.setText(_translate("VmSettings_ui", "Hardware"))
        self.userButton.setText(_translate("VmSettings_ui", "User"))
        self.proxiesButton.setText(_translate("VmSettings_ui", "Proxies"))
        self.label_2.setText(_translate("VmSettings_ui", "Comment"))
        self.label_3.setText(_translate("VmSettings_ui", "VM Name"))
        self.chkVmware.setText(_translate("VmSettings_ui", "VMware"))
        self.chkVbox.setText(_translate("VmSettings_ui", "Virtualbox"))
        self.chkParallels.setText(_translate("VmSettings_ui", "Paralells"))
        self.chkDesktop.setText(_translate("VmSettings_ui", "Desktop"))
        self.chkUpdate.setText(_translate("VmSettings_ui", "Updates"))
        self.chkVagrant.setText(_translate("VmSettings_ui", "Vagrant"))
        self.label_4.setText(_translate("VmSettings_ui", "Iso Name"))
        self.label_5.setText(_translate("VmSettings_ui", "Iso URL"))
        self.label_6.setText(_translate("VmSettings_ui", "Iso Hash"))
        self.label_7.setText(_translate("VmSettings_ui", "ISO Hash Algorithm"))
        self.label_11.setText(_translate("VmSettings_ui", "Iso Path"))
        self.label_8.setText(_translate("VmSettings_ui", "CPUs"))
        self.label_9.setText(_translate("VmSettings_ui", "Memory Size"))
        self.label_10.setText(_translate("VmSettings_ui", "Disk Size"))
        self.laUserName.setText(_translate("VmSettings_ui", "Ssh User Name"))
        self.laUserPassword.setText(_translate("VmSettings_ui", "Ssh User Password"))
        self.laVerifyPassword.setText(_translate("VmSettings_ui", "Verify Password"))
        self.laUserHomeDir.setText(_translate("VmSettings_ui", "User Home Dir"))
        self.laUserShell.setText(_translate("VmSettings_ui", "User Shell"))
        self.laUserComment.setText(_translate("VmSettings_ui", "User Long Name/Comment"))
        self.laHttp_proxy.setText(_translate("VmSettings_ui", "http_proxy"))
        self.laHttps_proxy.setText(_translate("VmSettings_ui", "https_proxy"))
        self.laFtpProxy.setText(_translate("VmSettings_ui", "ftp_proxy"))
        self.laRsyncProxy.setText(_translate("VmSettings_ui", "rsync_proxy"))
        self.laNoProxy.setText(_translate("VmSettings_ui", "no_proxy"))
