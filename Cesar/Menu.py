#!/usr/bin/env python3

"""
Menu pronto para programas de criptografia.
"""
import os, signal, cesar

def ajuda():

	print("Ajuda do código")
	
	input("\n\nPressione Enter para continuar")

def sobre():
	print ("Sobre:\n\
		\n\
		Explicação do código\n\
		Esse código executa a cifra de Cesar\n\
		É o segundo desafio proposto nas ferias de dez/14 pelo grupo de estudos criptográficos de Americana (GECA)\n\
	Versão:\n\
		\n\
		0.2 (05/02/15)\n\
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
		frase = input("Digite a frase a ser criptografada:  \b").replace(" ","").upper()
		chave = "1"
		cesar.cripto(frase, chave)
	elif menu is "2":
		frase = input("Digite a frase a ser descriptografada:  \b").replace(" ","").upper()
		chave = "2"
		cesar.cripto(frase, chave)
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
