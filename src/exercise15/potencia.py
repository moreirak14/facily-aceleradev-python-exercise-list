""" Faça um programa que peça dois números (base e expoente) e calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência 
nativa da linguagem.  """

def potencia():
     base = int(input('Digite a base: '))
     expoente = int(input('Digite o expoente '))
     calculo = base ** expoente
     print(f"Base {base} elevado ao expoente {expoente} é: {calculo}")
     

potencia()
