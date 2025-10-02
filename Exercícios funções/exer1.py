def idade(atual, nasc):
    return atual - nasc

nasc = int(input('Digite o ano de nascimento: '))
atual = int(input('Digite o ano atual: '))
idade = idade(atual, nasc)
print(f'A idade é {idade} anos.')