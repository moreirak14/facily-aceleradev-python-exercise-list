""" Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num 
vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0 """

def student_notes_vetor():
    alunos_acima = 0
    medias = []
    
    for aluno in range(5):
        
        notas = 0
        for nota in range(2):
            print("Digite a ", nota+1, "nota do ", aluno+1, "aluno")
            notas += int(input())

        medias.append(notas/2)

        if medias[aluno] >= 7.0:
            alunos_acima += 1
        
    print(f"Médias acima de 7: {alunos_acima}")

student_notes_vetor()
