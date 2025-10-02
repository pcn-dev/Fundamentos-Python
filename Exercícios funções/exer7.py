frutas = input('Digite os produtos separados por vírgula: ').split(',')
precos = input('Digite os preços separados por vírgula: ').split(',')

for fruta, preco in zip(frutas, precos):
    print(f'{fruta.strip()}: {preco.strip()}')