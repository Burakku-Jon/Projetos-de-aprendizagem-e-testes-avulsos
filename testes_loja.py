#começando importando as bibliotecas necessárias:
import pandas as pd
import numpy as np
import time as tm
import tkinter as tk

#criando o dicionário com os produtos disponíveis na loja:
produtos = {
    1 : {"nome": "Teclado magnético", "preço": 650.00, "quantidade": 15},
    2 : {"nome" : "Teclado mecânico", "preço": 300.00, "quantidade": 15},
    3 : {"nome" : "Monitor FHD 27", "preço": 600.00, "quantidade": 5},
    4 : {"nome" : "Monitor QHD 27", "preço": 900.00, "quantidade": 5},
    5 : {"nome" : "Monitor QHD 32", "preço": 1200.00, "quantidade": 5},
    6 : {"nome" : "Mouse gamer Razer Purgatory 6400 dpi", "preço": 100.00, "quantidade": 25},
    7 : {"nome" : "Mouse gamer Redragon cobra 10000 dpi", "preço": 250.00, "quantidade": 15},
    8 : {"nome" : "Headset gamer Havit h4008", "preço": 300.00, "quantidade": 25}
}
carrinho = []
class JanelaFlutuante:
    def __init__(self, master):
        self.master = master
        
# Configurações básicas da janela flutuante
        master.wm_overrideredirect(True)       # Remove bordas/barra
        master.attributes('-topmost', True)    # Sempre no topo
        master.geometry("1920x1080+200+200")      # Tamanho inicial
        master.config(bg="#2e2e2e")            # Cor de fundo escura
        
# Variáveis para guardar a posição do mouse no clique
        self.x_clique = 0
        self.y_clique = 0
        
# Cria a barra personalizada (para arrastar a janela)
        self.barra_movivel = tk.Frame(master, bg="#1c1c1c", height=30)
        self.barra_movivel.pack(fill="x", side="top")
        
# Vincula os eventos do mouse na barra cinza para poder arrastar
        self.barra_movivel.bind("<Button-1>", self.capturar_posicao)
        self.barra_movivel.bind("<B1-Motion>", self.mover_janela)
        
# Botão para fechar a janela flutuante
        self.botao_fechar = tk.Button(
            self.barra_movivel, text="X", fg="white", bg="#ff4d4d", 
            bd=0, command=master.destroy, width=3
        )
        self.botao_fechar.pack(side="right")
        
#Criando sistema de interação com o usuário:
        
#Testando a primeira interação com o usuário, criando um botão e uma label:
        self.label = tk.Label(master, text="Clique no botão abaixo:", fg="white", bg="#2e2e2e")
        self.label.pack(pady=10)
        
#Criando o botão que vai disparar a ação do usuário:
        self.botao_acao = tk.Button(master, text="Executar Ação", command=self.acao_do_usuario)
        self.botao_acao.pack(pady=5)

    def capturar_posicao(self, event):
# Guarda a posição do mouse no momento exato do clique
        self.x_clique = event.x
        self.y_clique = event.y

    def mover_janela(self, event):
# Calcula a nova posição com base no arrastar do mouse
        novo_x = self.master.winfo_x() + (event.x - self.x_clique)
        novo_y = self.master.winfo_y() + (event.y - self.y_clique)
        self.master.geometry(f"+{novo_x}+{novo_y}")
        
    def acao_do_usuario(self):
# Função disparada pelo botão interativo
        self.label.config(text="Ação executada com sucesso!")

# Inicializa o programa
raiz = tk.Tk()
app = JanelaFlutuante(raiz)
raiz.mainloop()
