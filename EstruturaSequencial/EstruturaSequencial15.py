ganha = float(input(print('Digite quanto você ganha: ')))
hora = float(input(print('Digite o número de horas trabalhadas no mês: ')))
salarioBruto = ganha*hora
print('+ Salário Bruto : R$ ', salarioBruto)
ir = salarioBruto*0.11
print('- IR (11%) : R$ ', ir)
inss = salarioBruto*0.08
print('- INSS (8%) : R$ ', inss)
sindicato = salarioBruto*0.05
print('- Sindicato (5%) : R$ ', sindicato)
salarioLiquido = salarioBruto - ir - inss - sindicato
print('= Salário Líquido : R$', salarioLiquido)