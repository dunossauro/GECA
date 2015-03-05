#!/usr/bin/env python3

"""
Menu pronto para programas de criptografia.
"""
import os, signal, rot13

def ajuda():

	print("Ajuda do código")
	
	input("\n\nPressione Enter para continuar")

def sobre():
	print ("Sobre:\n\
		\n\
		Esse código executa a cifra do Kama-sutra ou ROT13\n\
		E é o primeiro desafio proposto nas ferias de dez/14 pelo grupo de estudos criptográficos de Americana (GECA)\n\
	Versão:\n\
		\n\
	0.1 (09/12/2014)\n\
	0.2 (12/12/2014)\n\
	0.3 (06/01/2015)\n\
	0.4 (05/02/2015)\n\
		\n\
	Desevolvedores:\n\
	0.1 e 0.2\n\
		Eduardo F. Mendes(z4r4tustr4) 			mendesxeduardo@gmail.com\n\
		Jacomo Giovanetti						jacomogiovanettimn@gmail.com\n\
	0.3 e 0.4\n\
		Eduardo F. Mendes(z4r4tustr4) 			mendesxeduardo@gmail.com\n\
		\n\
		\n\
	Debug:\n\
		0.1\n\
		William G. Lopes(WgL) 					williangldzn@gmail.com\n")

	input("\n\nPressione Enter para continuar")

#função do menu inicial do programa e que recebe as entradas
def menu():
	#Menu inicial
	os.system('clear')

	print("\
	Kama sutra - ROt13\n\
	=== Menu ===\n\
	1. Criptografar ou Descriptografar\n\
	2. Ajuda\n\
	3. Sobre\n\
	4. Sair\n")

	menu = input(":")

	if menu is "1":
		frase = input("Digite a frase a ser criptografada:  \b").replace(" ","").upper()
		rot13.cripto(frase)
	elif menu is "2":
		ajuda()
	elif menu is "3":
		sobre()
	elif menu is "4":
		exit()

#Úm laço para manter o menu constante
def main():
	while True:
		menu()

main()
