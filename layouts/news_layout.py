# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'news_layout.ui'
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
        Form.resize(642, 498)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 602, 219))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setMaximumSize(QtCore.QSize(415, 16777215))
        self.line.setStyleSheet(_fromUtf8("background-color:white"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.titleBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.titleBrowser.setMaximumSize(QtCore.QSize(99999, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei Light"))
        font.setPointSize(11)
        self.titleBrowser.setFont(font)
        self.titleBrowser.setStyleSheet(_fromUtf8("font-size:11pt;font-family:\"Microsoft JhengHei Light\";background-color:transparent"))
        self.titleBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.titleBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.titleBrowser.setLineWidth(0)
        self.titleBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.titleBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.titleBrowser.setObjectName(_fromUtf8("titleBrowser"))
        self.verticalLayout.addWidget(self.titleBrowser)
        self.descBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.descBrowser.setMaximumSize(QtCore.QSize(99999, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei Light"))
        font.setPointSize(11)
        self.descBrowser.setFont(font)
        self.descBrowser.setStyleSheet(_fromUtf8("font-size:11pt;font-family:\"Microsoft JhengHei Light\";background-color:transparent"))
        self.descBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.descBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.descBrowser.setLineWidth(0)
        self.descBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descBrowser.setObjectName(_fromUtf8("descBrowser"))
        self.verticalLayout.addWidget(self.descBrowser)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "NEWS", None))
        self.titleBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">06 Jan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2016</p></body></html>", None))
        self.descBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft JhengHei Light\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">06 Jan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2016</p></body></html>", None))

