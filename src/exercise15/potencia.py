""" Faça um programa que peça dois números (base e expoente) e calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência 
nativa da linguagem.  """


def potencia(base, expoente):
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente "))
    return base ** expoente


if __name__ == "__main__":
    calculo = potencia(2, 2)
    print(f"{calculo}")
