def saudacao(hora):
    if 0 >= hora <12:
        return 'Bom dia!'
    elif 12 >= hora <= 18:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

horario = int(input('Digite a hora atual (0-23): '))

print(saudacao(horario))