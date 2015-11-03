import re

class map_texto:

	def __init__(self, arq ,dic={}, lista=[]):
		self.dic = dic
		self.lista = lista
		self.arq = arq

	def monta_lista(self,):
		arq = open(self.arq,'r').read()

		arq = re.sub('[\\n ]', '', arq)

		for x,y in enumerate(arq):
			self.dic[y] = x

	def cripto(self,):
		texto = input("Digite o texto a ser criptografado: ").lower()
		for i in texto:
			for j in (sorted(self.dic)):
				if i == j:
					self.lista.append(str(self.dic[i]))

a = map_texto("Mascara_Beale.txt")
a.monta_lista()
a.cripto()
print(" ".join(a.lista))
