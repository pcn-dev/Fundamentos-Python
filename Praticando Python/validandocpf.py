def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    return 'CPF válido.'


def chamar_cpf():
    while True:
        cpf = input('Digite o seu CPF: ')
        resultado = validar_cpf(cpf)
        print(resultado)
        if resultado == 'CPF válido.':
            break



def main():
    '''Essa função serve para exibir tudo do sistema'''
    chamar_cpf()


if __name__ == '__main__':
    main()