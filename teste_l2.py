import time as tm

class produto:
    def __init__(self, preço, quantidade,):
        self.preço = preço
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Este carro é um {self.marca} e sua cor é {self.cor}.")

class carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def exibir_itens(self):
        for item in self.itens:
            print(f"Produto: {item.nome}, Preço: {item.preço}, Quantidade: {item.quantidade}")

produtos = {
    "macarrao": produto(35.50, 20),
    "chocolate": produto(7.50, 10),
    "arroz": produto(36.00, 90),
    "suco": produto(5.00, 50)
}


while True:
    print("[1] Visualizar estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Visualizar carrinho.")
    print("[4] Finalizar compra.")
    print("[0] Sair.")
    selection = int(input("Escolha sua opção:"))

    if selection == 1:
        print(f"[visualizar estoque]")
        for key, content in produtos.items():
            print(f" Produto:{key} : Preço:{content.preço} : Quantidade:{content.quantidade}")

    elif selection == 2:
        print(f"[adicionar item ao carrinho]")

    elif selection == 3:
        print(f"[visualizar carrinho]")

    elif selection == 4:
        f_c = input("Deseja finalizar a compra? (s/n): ")
        if f_c.lower() == "s":
            print(f"[finalizar compra.]")
            tm.sleep(2)
            print(f"[finalizar compra..]")
            tm.sleep(2)
            print(f"[finalizar compra...]")
        else:
            print("Compra não finalizada.")

    elif selection < 0:
        print("Opção inválida")
        break
    else:
        print("Saindo...")