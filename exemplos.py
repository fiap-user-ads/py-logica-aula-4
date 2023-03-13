# decisão composta (if ... else)
'''
"""
    DADA UMA IDADE, VERIFICAR SE É MAIOR DE IDADE OU NÃO
"""

# obter idade
idade = int(input("Digite sua idade: "))

# condições
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''

# decisão encadeada (if ... elif ... else)
'''
"""
    CORREÇÃO DE NÚMERO POSITIVO, NEGATIVO OU NULO
"""

# obter número
num = float(input("Digite um número: "))

# condições encadeada
if num > 0:
    print("Positivo!")
elif num < 0:
    print("Negativo!")
else:
    print("Nulo!")
'''
