# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream, QUrl
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QLineEdit, QMainWindow, QVBoxLayout, QHBoxLayout
from PyQt5.QtNetwork import QNetworkProxyFactory, QNetworkRequest, QNetworkProxy

class Ui_MainWindow(object):
    def adjustLocation(self):
        # print('sduyfc')
        k = self.webView.url().toString()
        self.line_edit.setText(k)

    def adjustTitle(self):
##        print('')
        if 0<self.progress<100:
            MainWindow.setWindowTitle("%s (%s%%)" % (self.webView.title(), self.progress))
        else:
            MainWindow.setWindowTitle(self.webView.title())
        MainWindow.setWindowIcon(self.webView.icon())

    def setProgress(self, p):
##        print('')
        self.progress = p
        self.adjustTitle()

    def adjustTitle_home(self):
##        print('')
        if 0<self.ppr<100:
            MainWindow.setWindowTitle("%s (%s%%)" % ('Google', self.ppr))
        else:
            MainWindow.setWindowTitle('Google')

    def setProgress_2(self, p):
##        print('')
        self.ppr = p
        self.adjustTitle_home()

    def back(self):
        self.webView.back()

    def reload(self):
        self.webView.reload()

    def forword(self):
        self.webView.forward()

    def home(self):
        self.webView.load(QtCore.QUrl("http://www.google.com"))
        self.ppr = 0
        self.line_edit.setText("http://www.google.com")
        # MainWindow.setWindowTitle('Google')
        self.webView.loadProgress.connect(self.setProgress_2)

    def search(self):
        url = self.line_edit.text()
        self.webView.load(QtCore.QUrl(url))
        # self.webView.loadStarted.connect(self.adjustLocation)
        self.webView.loadFinished.connect(self.adjustLocation)
        self.webView.loadFinished.connect(self.adjustTitle)
        self.webView.loadProgress.connect(self.setProgress)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")


        self.progress = 0

##        fd = QFile(":/jquery.min.js")
##
##        if fd.open(QIODevice.ReadOnly | QFile.Text):
##            self.jQuery = QTextStream(fd).readAll()
##            fd.close()
##        else:
##            self.jQuery = ''


        MainWindow.resize(551, 467)
        ############################################################
        QNetworkProxyFactory.setUseSystemConfiguration(True)
        # QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, '192.168.1.107', 3128))
        ############################################################
        icon11 = QIcon()
        icon11.addPixmap(QPixmap("icons/option.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        ######################################################################
        self.tb_back = QToolButton(self.centralwidget)
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/back.png"), QIcon.Active, QIcon.Off)
        self.tb_back.setIcon(icon)
        self.tb_back.setObjectName("tb_back")
        self.horizontalLayout_3.addWidget(self.tb_back)

        ############################## Enter #######################################
        self.tb_back.clicked.connect(self.back)
        ############################################################################

        self.tb_reload = QToolButton(self.centralwidget)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/reload.png"), QIcon.Active, QIcon.Off)
        self.tb_reload.setIcon(icon1)
        self.tb_reload.setObjectName("tb_reload")
        self.horizontalLayout_3.addWidget(self.tb_reload)

        ############################## Enter #######################################
        self.tb_reload.clicked.connect(self.reload)
        ############################################################################

        self.tb_forword = QToolButton(self.centralwidget)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/forword.png"), QIcon.Active, QIcon.Off)
        self.tb_forword.setIcon(icon2)
        self.tb_forword.setObjectName("tb_forword")
        self.horizontalLayout_3.addWidget(self.tb_forword)

        ############################## Enter #######################################
        self.tb_forword.clicked.connect(self.forword)
        ############################################################################

        self.tb_home = QToolButton(self.centralwidget)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("icons/home.png"), QIcon.Active, QIcon.Off)
        self.tb_home.setIcon(icon3)
        self.tb_home.setObjectName("tb_home")
        self.horizontalLayout_3.addWidget(self.tb_home)

        ############################## Enter #######################################
        self.tb_home.clicked.connect(self.home)
        ############################################################################

        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout_3.addWidget(self.line_edit)

        ############################################################################

        self.tb_search = QToolButton(self.centralwidget)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("icons/search.png"), QIcon.Active, QIcon.Off)
        self.tb_search.setIcon(icon4)
        self.tb_search.setObjectName("tb_search")
        self.horizontalLayout_3.addWidget(self.tb_search)

        ############################## Enter #######################################
        self.tb_search.clicked.connect(self.search)
        ############################################################################

        self.tb_newtab = QToolButton(self.centralwidget)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap("icons/star.png"), QIcon.Active, QIcon.Off)
        self.tb_newtab.setIcon(icon5)
        self.tb_newtab.setObjectName("tb_newtab")
        self.horizontalLayout_3.addWidget(self.tb_newtab)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.webView = QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout_2.addWidget(self.webView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "divanshu"))
        self.tb_back.setText(_translate("MainWindow", "..."))
        self.tb_reload.setText(_translate("MainWindow", "..."))
        self.tb_forword.setText(_translate("MainWindow", "..."))
        self.tb_home.setText(_translate("MainWindow", "..."))
        self.tb_search.setText(_translate("MainWindow", "..."))
        self.tb_newtab.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    if len(sys.argv) > 1:
        url = QUrl(sys.argv[1])
    else:
        url = QUrl('http://www.google.com/ncr')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

