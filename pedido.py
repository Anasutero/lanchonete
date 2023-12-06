lanches = {1: "salada", 2: "coxinha", 3: "pizzas", 4: "Hamburguer", 5: "pão de queijo"}
bebidas = {1: "suco", 2: "agua", 3: "refrigerante", 4: "Energetico", 5: "Agua com gás"}
sobremesas = {1: "bolo", 2: "brigadeiro", 3: "sorvete", 4: "Pudim", 5: "Churros"}
pedido = {"lanches": [], "bebida": [], "sobremesas": []}


def pedido_lanche():
    print("Cardápio de lanches:")
    for indice, itens in lanches.items():
        print(f"{indice}: {itens}")
    indice = int(input("Insira o número do que deseja:"))

    if indice in lanches:
        pedido["lanches"].append(lanches[indice])
        print(f"O seu pedido escolhido foi: {lanches[indice]}")
    else:
        print("Índice inválido")


def pedido_bebidas():
    print("Cardápio de bebidas:")
    for indice, itens in bebidas.items():
        print(f"{indice}: {itens}")
    indice = int(input("Insira o número do que deseja:"))

    if indice in bebidas:
        pedido["bebida"].append(bebidas[indice])
        print(f"O seu pedido escolhido foi: {bebidas[indice]}")
    else:
        print("Índice inválido")


def pedido_sobremesas():
    print("Cardápio de sobremesas:")
    for indice, itens in sobremesas.items():
        print(f"{indice}: {itens}")
    indice = int(input("Insira o número do que deseja:"))

    if indice in sobremesas:
        pedido["sobremesas"].append(sobremesas[indice])
        print(f"O seu pedido escolhido foi: {sobremesas[indice]}")
    else:
        print("Índice inválido")


def finalizar_pedido():
    print("Comanda do pedido:")
    for categoria, itens in pedido.items():
        if itens:
            print(f"{categoria.capitalize()}:{', '.join(itens)}\n")

    resposta = input("Pedido está correto? s/n: ").strip().lower()
    if resposta == "s":
        with open("comanda.txt", "w") as arquivo:
            arquivo.write("Comanda\n")
            for categoria, itens in pedido.items():
                if itens:
                    arquivo.write(f"{categoria.capitalize()} : {' '.join(itens)}\n")
        print("Pedido finalizado, é salvo no arquivo da comanda")
        pedido.clear()
        print("Novo pedido:")
    elif resposta == "n":
        print("Pedido não finalizado, corrija seu pedido:")
    else:
        print("Resposta Inválida")


def main():
    while True:
        print("\nOpções de pedido:")
        print("1: Fazer pedido lanche")
        print("2: Fazer pedido bebida")
        print("3: Fazer pedido sobremesa")
        print("4: Finalizar pedido")
        print("5: Sair")
        opcao = int(input("Insira o número da opção desejada:"))

        if opcao == 1:
            pedido_lanche()
        elif opcao == 2:
            pedido_bebidas()
        elif opcao == 3:
            pedido_sobremesas()
        elif opcao == 4:
            finalizar_pedido()
        elif opcao == 5:
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

