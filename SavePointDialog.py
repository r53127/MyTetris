# -*- coding: utf-8 -*-

"""
Module implementing SavePointDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox

from Ui_SavePointDialog import Ui_Dialog


class SavePointDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SavePointDialog, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

    def setPointLabel(self, label_text):
        self.pointLabel.setText('您的得分是：' + label_text)
        self.lineEdit.setFocus()

    def checkLineEdit(self):
        """
        Slot documentation goes here.
        """
        a = len(self.lineEdit.text().strip())
        if a <= 0:
            QMessageBox.information(self, '提示', '请输入您的大名！')
            return False
        elif a > 10:
            QMessageBox.information(self, '提示', '大名不要超过10个字符！')
            return False
        else:
            return self.lineEdit.text()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.checkLineEdit():
            self.parent.saveData(self.lineEdit.text())
            self.close()


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()

