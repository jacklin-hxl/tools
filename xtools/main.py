import sys
import binascii
import hashlib

from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from xtui import Ui_Form
from xtoolsfunc import XToolsFunc

base64_method = ["encode","decode"]
hash_available = hashlib.algorithms_guaranteed

class MainUi(QMainWindow,QFileDialog,Ui_Form):
    def __init__(self,parent=None):
        super(MainUi,self).__init__(parent)
        self.setupUi(self)
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.setItemText(0,"base64")
        self.type_ComboBox.setItemText(1,"Hash")
        self.type_ComboBox.activated.connect(self.enc_type)
        self.confirm_Button.clicked.connect(self.confirm)
        self.open_Button.clicked.connect(self.openfile)
        for i in range(len(base64_method)):
            self.method_ComboBox.addItem("")
            self.method_ComboBox.setItemText(i,base64_method[i])
        

    def openfile(self):
        filedir = self.getOpenFileName(self,"open file","./","All Files (*)")[0]
        self.input_TextEdit.setText(filedir)


    def enc_type(self):
        self.method_ComboBox.clear()
        if self.type_ComboBox.currentText() == "Hash":
            hash_available_list = list(hash_available)
            for i in range(len(hash_available_list)):
                self.method_ComboBox.addItem("")
                self.method_ComboBox.setItemText(i,hash_available_list[i])
        else:
            for i in range(len(base64_method)):
                self.method_ComboBox.addItem("")
                self.method_ComboBox.setItemText(i,base64_method[i])

    def confirm(self):
        enc_type = self.type_ComboBox.currentText()
        method = self.method_ComboBox.currentText()
        value = self.input_TextEdit.toPlainText()
        if value:
            if enc_type == "base64":
                result = XToolsFunc.base64_method(method,value)
                self.ouput_TextBrowser.setText(result[0])
                self.output_label.setText(result[1])
            elif enc_type == "Hash":
                result = XToolsFunc.hash_method(method,value)
                self.ouput_TextBrowser.setText(result[0])
                self.output_label.setText(result[1])
        else:
            self.output_label.setText("无输入")
            self.ouput_TextBrowser.clear()

def main():
    app = QApplication(sys.argv)
    myUi = MainUi()
    myUi.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()