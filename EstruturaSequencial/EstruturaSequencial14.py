peso = float(input(print('Digite o peso total dos peixes em quilos: ')))
if (peso<=50):
    print('Não precisa pagar multa!')
else:
    excesso = peso - 50.0
    multa = excesso*4
    print('O excesso de peso foi de %.2f kg que gerou uma multa de %.2f reais.' %(excesso, multa))