#!/usr/bin/python 3
 
import string

alfabeto = string.ascii_uppercase
mensagem = input("Digite a mensagem:  ").upper().replace(" ","")
chave = input("Digite a chave:  ").upper().replace(" ","")
posicao = 0
resultado = ""

"""

mod_c = Módulo da chave
mod_a = Módulo do alfabeto
letra_m = Letra da mensagem
letra_c = letra da chave

"""
for letra_m in mensagem:

	mod_c = posicao % len(chave)
	letra_c = chave[mod_c]
	mod_a = (alfabeto.find(letra_m) + alfabeto.find(letra_c)) % 26
	resultado += alfabeto[mod_a]
	posicao += 1

print(resultado)
