total = 10

while total > 0:
    if total % 2 == 0:
        print(f'Faltam apenas {total} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {total} segundos restantes')
    total -= 1

print('Aproveite a promoção agora!')