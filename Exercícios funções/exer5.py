valores = input('Digite os valores das vendas: ').split()
convertidos = [float(valor) for valor in valores]

print(f'O total de vendas foi: {sum(convertidos)}')