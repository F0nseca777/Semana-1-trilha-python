import math
def questao():
    contador = 0
    valor= 2
    lista=[]
    while contador <10000:
        log= math.log(valor)
        formula= 1/(valor*log**2)
        lista.append(formula)
        soma = sum(lista)
        valor= valor+1
        contador = contador +1
    print('o valor de conevergencia é aproximadamente: ')
    print (soma)
questao()
