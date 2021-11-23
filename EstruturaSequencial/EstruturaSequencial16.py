area = float(input(print('O tamanho da área a ser pintada em metros quadrados: ')))
litros = area/3
if (litros%18 == 0):
    latas = litros//18
else:
    latas = litros//18 + 1
preçoTotal = latas*80
print('A quantidade de latas de tinta é de %d e o preço total foi de %.2f reais.' %(latas, preçoTotal))