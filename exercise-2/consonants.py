""" Faça um Programa que leia uma string e diga quantas consoantes foram lidas.
 Imprima as consoantes """

def consonants():
    palavra = input("Digite uma palavra: ")
    count = 0

    for letra in palavra:
        if letra in "bcdfghjklmnpqrstvxywz":
            count += 1

    print(f"A palavra '{palavra}' tem {count} consoantes.")
                 
consonants()
