tamanho = float(input(print('Digite o tamanho do arquivo (em MB): ')))
velocidade = float(input(print('Digite a velocidade do link de internet (em Mbps): ')))
tempo = (tamanho/velocidade)/60
print('O tempo aproximado de download do arquivo usando este link é de %.2f minutos.' %(tempo))