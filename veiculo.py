class Veiculo():
	"""Essa é a classe carro. Esta classe é utilizada para instanciar novos carros em nosso programa"""
	def __init__(self, cor, tipo_combustivel, potencia):
		self.__cor = cor
		self.__tipo_combustivel = tipo_combustivel
		self.__potencia = potencia
		self.__qtd_combustivel = 0
		self.__is_ligado = False
		self.__velocidade = 0

	def __del__(self):
		print("O objeto foi removido da memória. :)")

	def abastecer(self, qtd_combustivel):
		"""O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustivel do objeto carro"""
		self.__qtd_combustivel += qtd_combustivel

	def ligar(self);
		if self.__is_ligado:
			print("O carro já está ligado")
		else:
			self.__is_ligado = True

	def desligar(self):
		if self.__is_ligado == False:
			print("O carro já está desligado")
		else:
			self.is_ligado = False

	def acelerar(self, velocidade=10):
		if self.__is_ligado:
			self.__velocidade += velocidade
		else:
			print("O carro precisa estar ligado para ser acelerado")