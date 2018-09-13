# -*- coding: utf-8 -*-

"""
Module implementing SavePointDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
import sys
from PyQt5.QtWidgets import  QApplication

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
        self.parent=parent
        self.setupUi(self)



    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """

        self.accept()
    
    @pyqtSlot()
    def on_buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        self.reject()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a=SavePointDialog()
    a.show()
    sys.exit(app.exec_())
