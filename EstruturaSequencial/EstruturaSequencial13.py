altura = float(input(print('Digite sua altura: ')))
genero = int(input(print('Qual é o seu gênero(Homem=1;Mulher=0): ')))
if (genero==1):
    pesoIdeal = (72.7*altura) - 58
elif (genero==0):
    pesoIdeal = (62.1*altura) - 44.7
print('Peso ideal é igual a %.2f' %(pesoIdeal))