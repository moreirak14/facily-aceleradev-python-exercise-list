""" Faça um Programa que leia as idades e alturas de 10 alunos e determine 
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos """

def student_year_vetor():
    alunos_acima_13 = 0
    medias = []
    
    for aluno in range(10):
        
        altura = 0
        idade = 0
        for idade in range(1):
            print("Digite a idade do ", aluno+1, "aluno")
            idade += int(input())
        
        for altura in range(1):
            print("Digite a altura do ", aluno+1, "aluno")
            altura += float(input())

        if idade[aluno] >= 13:
            alunos_acima_13 += 1
             
    print(f"Médias com mais de 13 anos: {alunos_acima_13}")

student_year_vetor()
