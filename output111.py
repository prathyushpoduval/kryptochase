# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Prathyush Poduval\Desktop\Kryptochase\kryptochase\cops.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1174, 678)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 429, 761, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(263, 20, 20, 391))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(600, 20, 20, 391))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 231, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_30 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout.addWidget(self.label_30, 7, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 7, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 2, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 6, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.label_29 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.label_29, 5, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout.addWidget(self.label_28, 5, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 6, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 5, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 1, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 6, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 7, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 300, 211, 81))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pwp1 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pwp1.setObjectName(_fromUtf8("pwp1"))
        self.pwp1.clicked.connect(pwpG_clicked)
        self.horizontalLayout.addWidget(self.pwp1)
        self.pwp2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pwp2.setObjectName(_fromUtf8("pwp2"))
        self.horizontalLayout.addWidget(self.pwp2)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 40, 151, 341))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 430, 641, 141))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cyc1 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.cyc1.setObjectName(_fromUtf8("cyc1"))
        self.horizontalLayout_2.addWidget(self.cyc1)
        self.cyc2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.cyc2.setObjectName(_fromUtf8("cyc2"))
        self.horizontalLayout_2.addWidget(self.cyc2)
        self.rev1 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.rev1.setObjectName(_fromUtf8("rev1"))
        self.horizontalLayout_2.addWidget(self.rev1)
        self.rev2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.rev2.setObjectName(_fromUtf8("rev2"))
        self.horizontalLayout_2.addWidget(self.rev2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 30, 301, 361))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Cop2Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.Cop2Display.setObjectName(_fromUtf8("Cop2Display"))
        self.gridLayout_2.addWidget(self.Cop2Display, 1, 1, 1, 1)
        self.Cop5Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.Cop5Display.setObjectName(_fromUtf8("Cop5Display"))
        self.gridLayout_2.addWidget(self.Cop5Display, 3, 0, 1, 1)
        self.Cop6Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.Cop6Display.setObjectName(_fromUtf8("Cop6Display"))
        self.gridLayout_2.addWidget(self.Cop6Display, 3, 1, 1, 1)
        self.Cop4Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.Cop4Display.setObjectName(_fromUtf8("Cop4Display"))
        self.gridLayout_2.addWidget(self.Cop4Display, 2, 1, 1, 1)
        self.Cop3Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.Cop3Display.setObjectName(_fromUtf8("Cop3Display"))
        self.gridLayout_2.addWidget(self.Cop3Display, 2, 0, 1, 1)
        self.cop1Display = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.cop1Display.setObjectName(_fromUtf8("cop1Display"))
        self.gridLayout_2.addWidget(self.cop1Display, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.xDisplay = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.xDisplay.setObjectName(_fromUtf8("xDisplay"))
        self.verticalLayout_2.addWidget(self.xDisplay)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_30.setText(_translate("MainWindow", "TextLabel", None))
        self.label_26.setText(_translate("MainWindow", "TextLabel", None))
        self.label_21.setText(_translate("MainWindow", "TextLabel", None))
        self.label_19.setText(_translate("MainWindow", "TextLabel", None))
        self.label_16.setText(_translate("MainWindow", "TextLabel", None))
        self.label_29.setText(_translate("MainWindow", "TextLabel", None))
        self.label_28.setText(_translate("MainWindow", "TextLabel", None))
        self.label_25.setText(_translate("MainWindow", "TextLabel", None))
        self.label_18.setText(_translate("MainWindow", "TextLabel", None))
        self.label_27.setText(_translate("MainWindow", "TextLabel", None))
        self.label_23.setText(_translate("MainWindow", "TextLabel", None))
        self.label_17.setText(_translate("MainWindow", "TextLabel", None))
        self.label_22.setText(_translate("MainWindow", "TextLabel", None))
        self.label_24.setText(_translate("MainWindow", "TextLabel", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.label_20.setText(_translate("MainWindow", "TextLabel", None))
        self.pwp1.setText(_translate("MainWindow", "PushButton", None))
        self.pwp2.setText(_translate("MainWindow", "PushButton", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.cyc1.setText(_translate("MainWindow", "PushButton", None))
        self.cyc2.setText(_translate("MainWindow", "PushButton", None))
        self.rev1.setText(_translate("MainWindow", "PushButton", None))
        self.rev2.setText(_translate("MainWindow", "PushButton", None))
        self.Cop2Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.Cop5Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.Cop6Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">heelllo</p><p align=\"center\">hedd</p></body></html>", None))
        self.Cop4Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">heelllo</p><p align=\"center\">hedd</p></body></html>", None))
        self.Cop3Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.cop1Display.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.xDisplay.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


start()
