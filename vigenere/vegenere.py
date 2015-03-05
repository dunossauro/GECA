#!/usr/bin/python3

import string

"""
mod_c = Módulo da chave
mod_a = Módulo do alfabeto
letra_m = Letra da mensagem
letra_c = letra da chave
"""


def cripto(frase, chave, chaveador):
	
	alfabeto = string.ascii_uppercase
	resultado = ""
	posicao = 0

	print(chave)

	for letra_m in frase:

		mod_c = posicao % len(chave)
		letra_c = chave[mod_c]

		if chaveador is "1":
			mod_a = (alfabeto.find(letra_m) + alfabeto.find(letra_c)) % 26
		else:
			mod_a = (alfabeto.find(letra_m) - alfabeto.find(letra_c)) % 26
	
		resultado += alfabeto[mod_a]
		posicao += 1

	print(resultado)
	input("\n\nPressione Enter para continuar")
