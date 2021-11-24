area = float(input(print('O tamanho da área a ser pintada em metros quadrados: ')))
litros = area/6
if (litros%18 == 0):
    latas = litros//18
else:
    latas = litros//18 + 1
preçoLatas = latas*80
if (litros%3.6 == 0):
    galoes = litros//3.6
else:
    galoes = litros//3.6 + 1
preçoGaloes = galoes*25
print('A quantidade de latas de tinta é de %d e o preço total foi de %.2f reais.' %(latas, preçoLatas))
print('A quantidade de latas de tinta é de %d e o preço total foi de %.2f reais.' %(galoes, preçoGaloes))