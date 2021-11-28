""" Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. 
Imprima os três vetores """

""" Utilize range, em conjunto com o laço de repetição for, 
para criar uma sequência dentro do intervalo [0,20] e alimentar sua lista. """

""" Adicione um item ao final da lista chamando o método append. """

""" Use o laço de repetição for para iterar ao longo da lista. """

def vetor_impar_par():
    numeros = []
    par = []
    impar = []
    count_par = 0
    count_impar = 0

    for numero in range(20):
        numeros.append(int(input("Digite um numero: ")))

    for numero in range(20):
        if numeros[numero] % 2 == 0:
            par.append(numeros[numero])
            count_par += 1
        else:
            impar.append(numeros[numero])
            count_impar += 1

    print("Vetor com 20 numero: " + str(numeros))
    print(f"Vetor com {count_par} pares: " + str(par))
    print(f"Vetor com {count_impar} impares: " + str(impar))

vetor_impar_par()
