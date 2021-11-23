soma = 0
i = 0
for i in range(4):
    soma += float(input(print('Digite a nota do bimestre %d: ' %(i+1))))
print('A média dos bimestres foi de: %.2f' %(soma/4))
