""" Faça um programa que receba a temperatura média de cada mês do ano e armazene-as 
em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas 
as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ) """

def temperature_year():
    temperatura = []
    meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", 
    "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    for i in range(len(meses)):
        temperatura.append(float(input("Digite a temperatura do mes de " + meses[i] + ": ")))

    media_ano = sum(temperatura)/len(temperatura)
    print(f"Média do ano é: {media_ano}")

    for i in range(len(temperatura)):
        if temperatura[i] > media_ano:
            print(str(i+1) + " - " + meses[i])

temperature_year()
