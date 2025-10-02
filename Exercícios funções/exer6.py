numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

def separar_pares(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

# O list() serve para listar os valores selecionados e o filter() serve para filtrar certos itens de acordo com uma condição.
convertidos = list(filter(separar_pares, numeros))
# O ''.join() serve para unir todos os elementos de uma lista em uma unica string e o map() vai listar e alterar para str os valores.
print('Os números pares são:', ' '.join(map(str, convertidos)))


############################################################################################################################################

# Outra forma de realizar esse exercício


numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 