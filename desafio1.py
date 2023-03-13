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
if salarioBruto <= 1302:
    aliquota1 = salarioBruto * aliquota1
    salarioLiquido = salarioBruto - aliquota1
    print(f"Salário bruto: R${salarioBruto:.2f}\nINSS: R${aliquota1:.2f}\nSalário líquido: R${salarioLiquido:.2f}")

elif salarioBruto > 1302 and salarioBruto <= 2571.29:
    aliquota2 = salarioBruto * aliquota2
    salarioLiquido = salarioBruto - aliquota2
    print(f"Salário bruto: R${salarioBruto:.2f}\nINSS: R${aliquota2:.2f}\nSalário líquido: R${salarioLiquido:.2f}")

elif salarioBruto > 2571.29 and salarioBruto <= 3856.94:
    aliquota3 = salarioBruto * aliquota3
    salarioLiquido = salarioBruto - aliquota3
    print(f"Salário bruto: R${salarioBruto:.2f}\nINSS: R${aliquota3:.2f}\nSalário líquido: R${salarioLiquido:.2f}")

elif salarioBruto < 3856.94 or salarioBruto <= 7507.49:
    aliquota4 = salarioBruto * aliquota4
    salarioLiquido = salarioBruto - aliquota4
    print(f"Salário bruto: R${salarioBruto:.2f}\nINSS: R${aliquota4:.2f}\nSalário líquido: R${salarioLiquido:.2f}")

else:
    salarioLiquido = salarioBruto - aliquota5
    print(f"Salário bruto: R${salarioBruto:.2f}\nINSS: R${aliquota5:.2f}\nSalário líquido: R${salarioLiquido:.2f}")