""" Faça um programa completo utilizando classes e métodos que: 
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: 
i. tipoCombustivel. 
ii. valorLitro 
iii. quantidadeCombustivel 
b. Possua no mínimo esses métodos: 
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo 
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente. 
iii. alterarValor( ) – altera o valor do litro do combustível. 
iv. alterarCombustivel( ) – altera o tipo do combustível. 
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
c. OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. 
 """


class bombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(
        self, valor
    ):  # método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        litros = valor / self.quantidadeCombustivel
        self.alterarQuantidadeCombustivel(litros)
        return print(
            f"A quantidade de litros que foi colocada no veículo foi: {int(litros)} litros do tipo {self.tipoCombustivel}"
        )

    def abastecerPorLitro(
        self, litro
    ):  # método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        valor = litro * self.valorLitro
        self.alterarQuantidadeCombustivel(litro)
        return print(f"O valor a ser pago pelo cliente é: R$ {valor} reais")

    def alterarValor(self, valor_alterado):  # altera o valor do litro do combustível.
        alterar_valor = self.valorLitro = valor_alterado
        return alterar_valor

    def alterarCombustivel(self, valor, tipo):  # altera o tipo do combustível
        self.tipoCombustivel = tipo
        self.alterarValor(valor)
        return print(
            f"O valor agora é: {self.alterarValor} e o combustivel agora é: {self.tipoCombustivel}"
        )

    def alterarQuantidadeCombustivel(
        self, litros
    ):  # altera a quantidade de combustível restante na bomba
        self.quantidadeCombustivel = self.quantidadeCombustivel - litros
        return print(
            f"Quantidade de combustivel restante: {self.quantidadeCombustivel}"
        )


combustivel = bombaCombustível("ALCOOL", 4.89, 100)
combustivel.abastecerPorValor(50)
combustivel.abastecerPorLitro(10)
combustivel.alterarValor(7)
combustivel.abastecerPorValor(20)
combustivel.alterarCombustivel(7, "GASOLINA")
