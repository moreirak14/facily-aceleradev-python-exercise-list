""" Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça: 
a. mostre a quantidade de valores que foram lidos; 
b. exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
c. exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; 
d. calcule e mostre a soma dos valores; 
e. calcule e mostre a média dos valores; 
f. calcule e mostre a quantidade de valores acima da média calculada; 
g. calcule e mostre a quantidade de valores abaixo de sete; 
h. encerre o programa com uma mensagem. 
 """


i = int(input("Digite o numero: "))
while i > -1:
    i -= 1
    if i == -3:
        break
    print(i)
