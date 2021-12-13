""" Implemente uma classe chamada Carro de acordo com as seguintes regras: 
a. um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque; 
b. o consumo é especificado no construtor e o nível de combustível inicial é 0; 
c. forneça um método andar( ) que simula o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina; 
d. forneça um método obterGasolina( ), que retorna o nível atual de combustível; 
e. forneça um método adicionarGasolina( ), para abastecer o tanque.  """


class Carro():

    def __init__(self, medida_km, litro):
        self.consumo = self.consumo_combustivel(medida_km, litro)
        self.nivel_combustivel = 0

    def consumo_combustivel(self, medida_km, litro):
        return (medida_km / litro)

    def andar(self, medida_km):
        nivel_atual = self.nivel_combustivel - (medida_km / self.consumo)
        self.nivel_combustivel = nivel_atual
        return print (f'O carro andou {medida_km} quilometros e agora está com {int(self.nivel_combustivel)} litros')

    def obterGasolina(self):
        return print(f"O nivel do combustivel está em: {int(self.nivel_combustivel)} litros")

    def adicionarGasolina(self, add_gasolina):
        self.nivel_combustivel += add_gasolina
        return print(f'Foi adicionado {int(self.nivel_combustivel)} litros de combustivel')

    def __str__(self):
        return f"O carro andou {self.consumo_combustivel} quilometros e o nivel de combustivel é {self.nivel_combustivel}"


combustivel = Carro(10, 1)
combustivel.obterGasolina()
combustivel.adicionarGasolina(56)
combustivel.obterGasolina()
combustivel.andar(20)
combustivel.obterGasolina()
#print(combustivel)
