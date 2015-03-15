#!/usr/bin/env python3

"""
Menu pronto para programas de criptografia.
"""
import os, signal, playfair

def ajuda():

	print("Ajuda do código")
	
	input("\n\nPressione Enter para continuar")

def sobre():
	print ("Sobre:\n\
		\n\
		Explicação do código\n\
		Esse código executa a cifra de Playfair\n\
		\n\
		0.1 (14/03/15)\n\
		\n\
	Desevolvedor:\n\
		0.2\n\
		Eduardo F. Mendes(z4r4tustr4) 			mendesxeduardo@gmail.com")

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
		frase = input("Digite a frase a ser criptografada:  \b").replace(" ","").lower().replace("j","i")
		chave = input("Digite a chave de criptografia:  \b").replace(" ","").lower().replace("j","i")
		chaveador = "1"
		playfair.monta_matriz(chave)
		playfair.cripto(frase, chave, chaveador)
	elif menu is "2":
		frase = input("Digite a frase a ser descriptografada:  \b").replace(" ","").lower().replace("j","i")
		chave = input("Digite a chave de decriptografia:  \b").replace(" ","").lower().replace("j","i")
		chaveador = "2"
		playfair.monta_matriz(chave)
		playfair.cripto(frase, chave, chaveador)
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
