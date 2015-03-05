#!/usr/bin/env python3

"""
Menu pronto para programas de criptografia.
"""
import os, signal, <arquivo>

def ajuda():

	print("Ajuda do código")
	
	input("\n\nPressione Enter para continuar")

def sobre():
	print ("Sobre:\n\
		\n\
		Explicação do código\n\
	Versão:\n\
		\n\
		0.1 (xx/xx/xx)\n\
		\n\
	Desevolvedores:\n\
		0.1\n\
			Nome (apelido)	email@mail.com\n\
		\n\
	Debug:\n\
		0.1\n\
			nome (apelido)			mail@mail.com\n")

	input("\n\nPressione Enter para continuar")

#função do menu inicial do programa e que recebe as entradas
def menu():
	#Menu inicial
	os.system('clear')

	print("	=== Menu ===\n\
	1. Criptografar\n\
	2. Descriptografar\n\
	3. Ajuda\n\
	4. Sobre\n\
	5. Sair\n")

	menu = input(":")

	if menu is "1":
		entradaLimpa = input("Digite a frase a ser criptografada:  \b")
		entradaLimpa = entradaLimpa.replace(" ","")		
		entradaLimpa = entradaLimpa.upper()
		frase = list(entradaLimpa)
		rot13.cripto(frase)
	elif menu is "2":
		entradaSuja = input("Digite a frase a ser descriptografada:  \b")
		entradaSuja = entradaSuja.replace(" ","")
		entradaSuja = entradaSuja.upper()
		frase = list(entradaSuja)
		rot13.cripto(frase)
	elif menu is "3":
		ajuda()
	elif menu is "4":
		sobre()
	elif menu is "5":
		exit()

#Úm laço para manter o menu constante
def main():
	while True:
		menu()

main()
