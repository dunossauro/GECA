import string
from os import system

system("clear")
alfabeto_limpo = string.ascii_uppercase
alfabeto_sujo = string.punctuation
texto_sujo = ""

palavra = input("Digite a o texto claro: ").upper()

for x in palavra:
	a = alfabeto_limpo.find(x)
	texto_sujo += alfabeto_sujo[a]

print(texto_sujo)
