def calcular_valor_total(valor_unitario: float, quantidade: int)-> float:
    ''' 
       CALCULA O VALOR DE UM PRODUTO COM BASE EM SEU VALOR UNITÁRIO E QUANTIDADE,
     CONSIDERANDO OS DESCONTOS APLICADO.   

     ARGS:
        VALOR_UNITÁRIO (FLOAT): VALOR UNITÁRIO DO PRODUTO.
        QUANTIDADE (INT): QUANTIDADE DESEJADA DO PRODUTO.

     RETURN:
        TUPLA [FLOAT, FLOAT]: TUPLA CONTENDO OS VALORES SEM DESCONTO E COM DESCONTO, RSPECTIVAMENTE.

    '''
    # NO DESCONTO O COMPLETO DE ATÉ 1 É O VALOR DO DESCONTO
    # EX: 0.85 TEM 15% DE DESCONTO -> 1 - 0.85 = 0.15

    desconto = 1

    # CALCULE O DESCONTO COM BASE NA QUANTIDADE DE PRODUTO COMPRADO.

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95

    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90

    elif quantidade >= 1000:
        desconto = 0.85



    #CALCULA O VALOR TOTAL COM DESCONTO E SEM DESCONTO.

    valor_com_desconto = valor_unitario * desconto * quantidade 
    valor_sem_desconto = valor_unitario * quantidade 

    return valor_sem_desconto, valor_com_desconto


if __name__ == '__main_ex1__':

    valor_unitario = float(input("valor unitário do produto"))
    quantidade = int(input("quantidade"))

    valor_sem_desconto, valor_com_desconto = calcular_valor_total (valor_unitario, quantidade)

    print(f"valor total sem desconto: {valor_sem_desconto:.2f}R$")
    print(f"valor total_com_desconto: {valor_com_desconto:.2f}R$")

    






