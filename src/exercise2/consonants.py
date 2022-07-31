""" Faça um Programa que leia uma string e diga quantas consoantes foram lidas.
 Imprima as consoantes """


def consonants(palavra: str):
    return palavra


if __name__ == "__main__":
    palavra = consonants("kaique")

    count = 0

    for letra in palavra:
        if letra in "bcdfghjklmnpqrstvxywz":
            count += 1
            print(f"As consoantes são: {letra}")
    print(f"As quantidades de consoantes são: {count}")
