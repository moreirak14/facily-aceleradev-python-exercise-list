""" Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as 
    notas lidas e a respectiva média. """

def student_notes():
    note1 = float(input('Digite a primeira nota: '))
    note2 = float(input('Digite a segunda nota: '))
    note3 = float(input('Digite a terceira nota: '))
    note4 = float(input('Digite a quarta nota: '))
    media = (note1 + note2 + note3 + note4) / 4
    print (f'A nota do aluno é: {media}')

student_notes()
