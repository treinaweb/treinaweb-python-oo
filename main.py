import carro, moto

uno_vermelho = carro.Carro("vermelho", 4, "Flex", 1.0, 4)
uno_vermelho.ligar()
print(uno_vermelho._libras)
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(20)
print(uno_vermelho.velocidade)
print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")

moto_vermelha = moto.Moto("Vermelha", "Gasolina", 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha.is_ligado)

