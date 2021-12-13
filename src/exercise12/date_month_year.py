""" Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário 
e imprima a data com o nome do mês por extenso. 
Ex: Data de Nascimento: 29/10/1973 
Você nasceu em 29 de Outubro de 1973.  """

def date_month_year():
    meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", 
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    dia, mês, ano = input("Data de Nascimento: ").split('/')

    print ("Você nasceu em " + "%s de %s de %s" %(dia, meses[int(mês) - 1], ano))

date_month_year()
