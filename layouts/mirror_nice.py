# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirror_nice.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(771, 767)
        Form.setStyleSheet(_fromUtf8("QWidget{background-color:black;color:white;}QLabel{font-size:50pt;font-family:}\n"
"font: 25 8pt \"HP Simplified Light\";\n"
""))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 747, 759))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.globalGrid = QtGui.QGridLayout(self.layoutWidget)
        self.globalGrid.setObjectName(_fromUtf8("globalGrid"))
        self.dayLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.dayLabel.setFont(font)
        self.dayLabel.setStyleSheet(_fromUtf8("font-size:40pt"))
        self.dayLabel.setObjectName(_fromUtf8("dayLabel"))
        self.globalGrid.addWidget(self.dayLabel, 0, 0, 2, 3)
        self.tempLabel = QtGui.QLabel(self.layoutWidget)
        self.tempLabel.setStyleSheet(_fromUtf8("font-size:30pt"))
        self.tempLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.globalGrid.addWidget(self.tempLabel, 4, 1, 1, 1)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet(_fromUtf8("background-color:white"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.globalGrid.addWidget(self.line, 2, 0, 1, 4)
        self.imgLabel = QtGui.QLabel(self.layoutWidget)
        self.imgLabel.setStyleSheet(_fromUtf8("background-color:transparent"))
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Downloads/cloud (1).png")))
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))
        self.globalGrid.addWidget(self.imgLabel, 4, 0, 1, 1)
        self.timeLabel = QtGui.QLabel(self.layoutWidget)
        self.timeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.globalGrid.addWidget(self.timeLabel, 3, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setStyleSheet(_fromUtf8("font-size:16pt"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.globalGrid.addWidget(self.label_2, 7, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_3.setStyleSheet(_fromUtf8("background-color:white"))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.globalGrid.addWidget(self.line_3, 8, 0, 1, 4)
        self.dateBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.dateBrowser.setMaximumSize(QtCore.QSize(99999, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei Light"))
        font.setPointSize(11)
        self.dateBrowser.setFont(font)
        self.dateBrowser.setStyleSheet(_fromUtf8("font-size:11pt;font-family:\"Microsoft JhengHei Light\";background-color:transparent"))
        self.dateBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.dateBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.dateBrowser.setLineWidth(0)
        self.dateBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dateBrowser.setObjectName(_fromUtf8("dateBrowser"))
        self.globalGrid.addWidget(self.dateBrowser, 1, 3, 1, 1)
        self.descBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.descBrowser.setMaximumSize(QtCore.QSize(16777215, 9999999))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(18)
        self.descBrowser.setFont(font)
        self.descBrowser.setStyleSheet(_fromUtf8("background-color:transparent; font-size:18pt;font-family:\"Roboto\""))
        self.descBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.descBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.descBrowser.setLineWidth(0)
        self.descBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descBrowser.setObjectName(_fromUtf8("descBrowser"))
        self.globalGrid.addWidget(self.descBrowser, 5, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.globalGrid.addItem(spacerItem, 3, 4, 1, 1)
        self.newsBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.newsBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.newsBrowser.setStyleSheet(_fromUtf8("font-size:10pt"))
        self.newsBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.newsBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.newsBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.newsBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.newsBrowser.setObjectName(_fromUtf8("newsBrowser"))
        self.globalGrid.addWidget(self.newsBrowser, 9, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.globalGrid.addItem(spacerItem1, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.dayLabel.setText(_translate("Form", "Saturday", None))
        self.tempLabel.setText(_translate("Form", "8°", None))
        self.timeLabel.setText(_translate("Form", "11:20", None))
        self.label_2.setText(_translate("Form", "News", None))
        self.dateBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">06 Jan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2016</p></body></html>", None))
        self.descBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei Light\'; font-size:14pt;\">PARTLY CLOUDY</span></p></body></html>", None))

