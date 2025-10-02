valor = float(input('Digite o total de despesas do mês (R$): '))

if valor > 3000:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Dentro do limite de orçamento do mês.')