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
        Form.resize(531, 603)
        Form.setStyleSheet(_fromUtf8("QWidget{background-color:darkgrey;color:white;}QLabel{font-size:50pt;font-family:\"Microsoft JhengHei Light\"}"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 531, 409))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.globalGrid = QtGui.QGridLayout(self.widget)
        self.globalGrid.setObjectName(_fromUtf8("globalGrid"))
        self.imgLabel = QtGui.QLabel(self.widget)
        self.imgLabel.setStyleSheet(_fromUtf8("background-color:transparent"))
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setPixmap(QtGui.QPixmap(_fromUtf8("E:/Downloads/cloud (1).png")))
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))
        self.globalGrid.addWidget(self.imgLabel, 4, 0, 1, 1)
        self.dayLabel = QtGui.QLabel(self.widget)
        self.dayLabel.setStyleSheet(_fromUtf8("font-size:40pt"))
        self.dayLabel.setObjectName(_fromUtf8("dayLabel"))
        self.globalGrid.addWidget(self.dayLabel, 0, 0, 2, 3)
        self.timeLabel = QtGui.QLabel(self.widget)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.globalGrid.addWidget(self.timeLabel, 3, 0, 1, 3)
        self.tempLabel = QtGui.QLabel(self.widget)
        self.tempLabel.setObjectName(_fromUtf8("tempLabel"))
        self.globalGrid.addWidget(self.tempLabel, 4, 1, 1, 2)
        self.dateBrowser = QtGui.QTextBrowser(self.widget)
        self.dateBrowser.setMaximumSize(QtCore.QSize(99999, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei Light"))
        font.setPointSize(11)
        self.dateBrowser.setFont(font)
        self.dateBrowser.setStyleSheet(_fromUtf8("font-size:11pt;font-family:\"Microsoft JhengHei Light\";background-color:transparent"))
        self.dateBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.dateBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.dateBrowser.setLineWidth(0)
        self.dateBrowser.setObjectName(_fromUtf8("dateBrowser"))
        self.globalGrid.addWidget(self.dateBrowser, 1, 3, 1, 1)
        self.descBrowser = QtGui.QTextBrowser(self.widget)
        self.descBrowser.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei Light"))
        font.setPointSize(18)
        self.descBrowser.setFont(font)
        self.descBrowser.setStyleSheet(_fromUtf8("font-family:\"Microsoft JhengHei Light\";background-color:transparent; font-size:18pt"))
        self.descBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.descBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.descBrowser.setLineWidth(0)
        self.descBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descBrowser.setObjectName(_fromUtf8("descBrowser"))
        self.globalGrid.addWidget(self.descBrowser, 5, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.globalGrid.addItem(spacerItem, 1, 4, 1, 1)
        self.line = QtGui.QFrame(self.widget)
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet(_fromUtf8("background-color:white"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.globalGrid.addWidget(self.line, 2, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.dayLabel.setText(_translate("Form", "Saturday", None))
        self.timeLabel.setText(_translate("Form", "11:20", None))
        self.tempLabel.setText(_translate("Form", "8°", None))
        self.dateBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">06 Jan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2016</p></body></html>", None))
        self.descBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei Light\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">PARTLY CLOUDY</span></p></body></html>", None))

