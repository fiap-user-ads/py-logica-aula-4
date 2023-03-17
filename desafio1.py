"""
  DADO O SALÁRIO DE UM FUNCIONÁRIO, CALCULAR QUANTO ELE PAGA DE
  INSS, CONSIDERANDO A TABELA. QUEM GANHAR ACIMA DO TETO
  PAGARÁ R$1051 FIXO.
  AO FINAL EXIBIR O SALÁRIO O SALÁRIO BRUTO, VALOR DO INSS E O SALÁRIO LÍQUIDO

  ---
  entrada: 1000

  salário bruto: 1000
  INSS: 75
  salário líquido: 925
"""

# obter salário
salarioBruto = float(input("Digite o seu salário: R$"))

aliquota1 = 0.075
aliquota2 = 0.09
aliquota3 = 0.12
aliquota4 = 0.14
aliquota5 = 1051

# condições
if salarioBruto >= 0 and salarioBruto <= 1302:
    inss = salarioBruto * aliquota1

elif salarioBruto > 1302 and salarioBruto <= 2572.29:
    inss = salarioBruto * aliquota2

elif salarioBruto > 2571.29 and salarioBruto <= 3856.94:
    inss = salarioBruto * aliquota3

elif salarioBruto < 3856.94 and salarioBruto <= 7507.49:
    inss = salarioBruto * aliquota4

else:
    inss = salarioBruto - aliquota5

salarioLiquido = salarioBruto - inss

print(f"""
Sálario...........: R$ {salarioBruto:9.2f}
INSS..............: R$ {inss:9.2f}
Salário Líquido...: R$ {salarioLiquido:9.2f}
""")
