while True:
    try:
        valor = float(input('Digite o valor da conta: '))
        porcentagem = float(input('Digite a porcentagem da gorjeta: '))
        break
    except ValueError:
        print('Valor informado não aceito.')
   
gorjeta = valor*(porcentagem/100)

if gorjeta < 1:  
    print(f'\nO valor da gorjeta ficou {gorjeta:.2f} centavos!')
else:
    print(f'\nO valor da gorjeta ficou {gorjeta:.2f} reais!')
   
total = valor+(valor*(porcentagem/100))

if total < 1:
    print(f'O valor total da compra é de: {total:.2f} centavos!')
else:
    print(f'O valor total da compra é de: {total:.2f} reais!')