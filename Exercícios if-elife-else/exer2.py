a = int(input('Informe os dias para a atividade A: '))
b = int(input('Informe os dias para a atividade B: '))
c = int(input('Informe os dias para a atividade C: '))

if a > 0 and b > 0 and c > 0:
    print('A soma dos números é: ', a + b + c)
else:
    print('Erro: Os dias não podem ser negativos.')