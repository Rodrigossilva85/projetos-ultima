def calcular_total_pedido(codigo_pedido):

    cardapio = {
        100:("cachorro quente", 9.0),
        101:("cachorro quente duplo", 11.0),
        102:("x-egg", 12.0),
        103:("x-salada", 12.0),
        104:("x-bacon", 14.0),
        105:("x-tudo", 17.0),
        200:("refrigerante lata", 5.0),
        201:("chá gelado", 4.0)
    }
    total = 0.0
    # variavel que armazena o valor total do pedido.

    for codigo in codigo_pedido:
    # percorrer a lista de códigos de produtos pedidos.

        if codigo in cardapio:
    # recupera as informações do produto a partir do cardápio e adiciona ao código.

            produto, valor = cardapio [codigo]
            print(f" VOCÊ PEDIU UM {produto} NO VALOR DE: {valor:.2f}R$")

            total += valor

        else:
            print("opção inválida")
    
    return total

if __name__ == " __main__":
    # mostrar o cardápio.

    cardapio = ''' 
*********************************** cardápio ****************************************************

CÓDIGO                              DESCRIÇÃO                               VALOR

100                            CACHORRO QUENTE                             9.0
101                            CACHORRO QUENTE DUPLO                       11.0
102                            X-EGG                                       12.0
103                            X-SALADA                                    12.0
104                            X-BACON                                     14.0
105                            X-TUDO                                      17.0
200                            REFRIGERANTE LATA                            5.0
201                            CHÁ GELADO                                   4.0

'''

    print(cardapio)


# lista de código que armazena o código dos produtos pedidos.
    codigos = []

# recebe o primeiro código de produto do usuário.
    codigo = int(input(" Entre com o código desejado"))  

    while True:
        # verifica se o código do produto é valido se consta no cardápio.

        if codigo in [100, 101, 102, 103, 104, 105, 200, 201]:
            codigos.append(codigo)  

        else:
            print("opção inválida")

            print("deseja edir alguma coisa?")
            print("1 - sim")
            print("2 - não")

            pedir_mais = int(input())

            if pedir_mais == 2:
                break

            codigo = int(input(" Entre com o código desejado:"))
        total = calcular_total_pedido(codigos)
        print(f" O total a ser pago é: {total:.2f}R$")


