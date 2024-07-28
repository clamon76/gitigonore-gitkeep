print("olá mundo!") 
print("Quem bom que você está aqui hoje")
print("Deus sempre sempre em primeiro lugar")
print("Jesus te ama")  
print("DEUS é amor")

from random import randint
from PyQt5 import QtWidgets, uic
janela=QtWidgets.QApplication([])
interface=uic.loadUi ("hello_interface.ui")
def PRINT():
    interface.label.setText(str(randint(0,700)))
