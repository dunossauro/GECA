import re

class map_texto:

    def __init__(self, arq):
        self.dic = {}
        self.lista = []
        self.arq = arq

    def monta_lista(self,):
        arq = open(self.arq,'r').read()

        arq = re.sub('[\\n ]', ' ', arq)

        #[self.dic[y] = x for x,y in enumerate(arq)]

        arq = arq.split()

        for x,y in enumerate(arq):
            self.dic[y] = x

        print(self.dic)
    def cripto(self,):

        texto = input("Digite o texto a ser criptografado: ").lower()

        [self.lista.append(str(self.dic[i])) for i in texto.split() for j in sorted(self.dic) if i == j]

a = map_texto("beale.txt")
a.monta_lista()
a.cripto()
print(" ".join(a.lista))
