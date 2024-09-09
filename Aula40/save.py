import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton

def main():
    def mudarNome():
        nome = inputNome.text()
        rotuloMensagem.setText(f"Hello {nome}!")
        rotuloMensagem.adjustSize()
        
    app = QApplication(sys.argv)
    janela = QWidget()
    janela.setWindowTitle("Primeira Janela")
    
    janela.setGeometry(300,100,400,300)
    
    #Criar os componentes
    rotuloMensagem = QLabel("Hello World", janela)
    
    rotuloMensagem.move(150,0)
    
    
    
    inputNome = QLineEdit(janela)
    inputNome.move(150,50)
    
    
    botaoEnviar = QPushButton("Enviar", janela)
    botaoEnviar.move(150, 100)
    
    botaoEnviar.clicked.connect(mudarNome)
    
    janela.show()
    sys.exit(app.exec())
    

    
    
main()