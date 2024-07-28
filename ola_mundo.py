print("olá mundo!") 
print("Quem bom que você está aqui hoje")
print("Deus sempre sempre em primeiro lugar")
print("Jesus te ama")  
print("DEUS é amor")

from random import randint
from PyQt5 import QtWidgets, uic

# Carrega a interface do arquivo hello_interface.ui
janela = QtWidgets.QApplication([])
interface = uic.loadUi("hello_interface.ui")

# Função para exibir "Deus é Amor" quando o botão for clicado
def exibir_deus_amor():
    interface.label.setText("Deus é Amor")

# Conecta o botão à função
interface.pushButton.clicked.connect(exibir_deus_amor)

# Exibe a interface
interface.show()
janela.exec_()
