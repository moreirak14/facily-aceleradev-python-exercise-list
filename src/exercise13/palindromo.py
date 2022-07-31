""" Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita
da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. 
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é
o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma sequência de caracteres e diga se esta é um palíndromo ou não.  """


def palindromo():

    frase = (
        str(input("Digite uma frase: ")).strip().upper()
    )  # strip = elimina os espaços antes e depois e o upper = a frase é convertida para caixa alta
    palavras = frase.split()  # gera um vetor da minha frase
    junto = "".join(palavras)  # pega o vetor e junta sem espaços em uma variavel
    inverso = ""
    for letra in range(
        len(junto) - 1, -1, -1
    ):  # foi na ultima letra da frase e foi lendo da direita para a esquerda
        inverso += junto[letra]
    if inverso == junto:  # compara a frase invertida com a variavel da frase toda junta
        print("É Palindromo!")
    else:
        print("Não é um Palindromo!")


palindromo()
