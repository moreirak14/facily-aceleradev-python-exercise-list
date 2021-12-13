""" Numa eleição existem três candidatos. Faça um programa que peça o número total 
de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato. """

def eleicao():
    voto1 = 0
    voto2 = 0
    voto3 = 0

    eleitores = int(input("Digite o total de eleitores para a votação: "))

    for i in range(eleitores):

        for voto in range(5):
            votos = int(input(f"Candidatos, votem em 1 ou 2 ou 3: "))
            if (votos == 1):
                voto1 = voto1 + 1
            elif (votos == 2):
                voto2 = voto2 + 1
            elif (votos == 3):
                voto3 = voto3 + 1
            else:
                return print("Numero de voto invalido")
    
    print(f"O candidato 1 votou {voto1} vezes")
    print(f"O candidato 2 votou {voto2} vezes")
    print(f"O candidato 3 votou {voto3} vezes")

eleicao()
