import string
from os import system

system("clear")
alfabeto_limpo = string.ascii_uppercase
alfabeto_sujo = string.punctuation
texto_sujo = ""
texto_limpo = ""

palavra = input("Digite a o texto claro: ").upper()

#Criptografar
for x in palavra:
	a = alfabeto_limpo.find(x)
	texto_sujo += alfabeto_sujo[a]

print(texto_sujo)

#Descriptografar
for x in texto_sujo:
	a = alfabeto_sujo.find(x)
	texto_limpo += alfabeto_limpo[a]

print(texto_limpo)
