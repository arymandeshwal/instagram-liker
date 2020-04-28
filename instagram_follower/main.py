#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
import test


# In[5]:


class Insta(QDialog):
    def __init__(self):
        super(Insta,self).__init__()
        loadUi('my_layout_2.ui',self)
        self.setWindowTitle('Instagram_followers_generator')
        self.pushButton.clicked.connect(self.on_push)
    
    @pyqtSlot()
    def on_push(self):
        test.run(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text())
        self.label_4.setText('Working')
        self.lineEdit_2.setText('**********')


# In[6]:


app = QApplication(sys.argv)
widget = Insta()
widget.show()
sys.exit(app.exec_())


# In[ ]:




