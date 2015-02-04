#!/bin/python3.4

#imports

import os, signal

#Função que executa a Cifra de cesar
def cripto(entrada,b):
"""
Essa parte do código foi baseada nesse link: http://pastebin.com/W6WGW3JE

E apesar de não resolver o problema do corpo finito e sim andar pela tabela ASCII já possível se fazer algo.
"""

	a=str()
	for x in entrada:
		if b == "0":
 			a +=(chr(ord(x)+3))
		if b == "1":
			a +=(chr(ord(x)-3))
	
	

	#Saida

	print("\n\n Frase: " + a)

	input("\n\nPressione Enter para continuar")

#função do menu inicial do programa
def menu():
	#Menu inicial
	os.system('clear')

	print("\
Cifra de Cesar\n\
=== Menu ===\n\
1. Criptografar\n\
2. Descriptografar\n\
	")


"""
A função replace remove os espaços em branco, para a analise de frequencia se tornar um pouco mais "complicada"
A função Upper está lá porque antigamente eram usados os caracteres maiusculos no texto criptografado
A variável b representa um chaveador, quando ativo a def cripto() faz descriptografia
quando inativo criptografia
"""

	menu = input(":")
	if menu == "1":
		entrada = input("Digite a frase a ser criptografada: \b")
		entrada = entrada.replace(" ","")		
		entrada = entrada.upper()
		b = "0"
		cripto(entrada,b)
	elif menu == "2":
		entrada = input("Digite a frase a ser descriptografada: \b")
		entrada = entrada.upper()
		entrada = entrada.replace(" ","")
		b = "1"
		cripto(entrada,b)

#Úm laço para manter o menu constante
def main():
	while True:
		menu()

main()
