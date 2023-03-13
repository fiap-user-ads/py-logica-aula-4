"""
  DADO 3 VALORES PELO USUÁRIO, EXIBIR O MAIOR VALOR
"""

# obter os 3 valores
primeiro = int(input("Primeiro numero: "))
segundo  = int(input("Segundo numero : "))
terceiro = int(input("Terceiro numero: "))

# calcular qual é o maior valor
maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

# Exibir o maior número
print(f"---\nO maior valor é: {maior}")