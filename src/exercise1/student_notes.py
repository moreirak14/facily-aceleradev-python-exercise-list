""" Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as 
    notas lidas e a respectiva média. """


def student_notes(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4


if __name__ == "__main__":
    media = student_notes(7, 7, 8, 8)
    print(f"A nota do aluno é: {media}")
