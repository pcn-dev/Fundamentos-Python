hora = int(input('Digite a hora atual (formato 24 horas): '))

if hora >= 8 and hora <= 18:
    print('Acesso Liberado')
else:
    print('Acesso Negado')