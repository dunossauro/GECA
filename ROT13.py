#!/bin/python3.4

#imports

import os, signal

#Função que executa a rot13
def cripto(frase):
	
	#Code

	alfabeto1 = "ABCDEFGHIJKLM"
	alfabeto2 = "NOPQRSTUVWXYZ"

	#alfabetos especiais

	alfabetoA = "ÁÃÀÄÂ"
	alfabetoE = "ÉÊËÈẼ"
	alfabetoI = "ÍÌĨÏÎ"
	alfabetoO = "ÓÒÕÔÖ"
	alfabetoU = "ÚÙÜŨÛ"
	alfabetoC = "Ç"


	for x in range(0, len(frase)):

		a = 0	
		

		for y in range(0, len(alfabeto1)):
		
			if frase[x] == alfabeto1[y]:
				frase[x] = alfabeto2[y]
				a = 1
		
		if a != 1:

			for y in range(0, len(alfabeto2)):

				if frase[x] == alfabeto2[y]:
					frase[x] = alfabeto1[y]
					a = 1

		if a != 1:
		
			for y in range(0, len(alfabetoA)):

				if frase[x] == alfabetoA[y]:
					frase[x] = "N"
					a = 1
		if a != 1:
		
			for y in range(0, len(alfabetoE)):

				if frase[x] == alfabetoE[y]:
					frase[x] = "R"
					a = 1

		if a != 1:
		
			for y in range(0, len(alfabetoI)):

				if frase[x] == alfabetoI[y]:
					frase[x] = "V"
		
		if a != 1:
		
			for y in range(0, len(alfabetoO)):

				if frase[x] == alfabetoO[y]:
					frase[x] = "B"
					a = 1
		if a != 1:
		
			for y in range(0, len(alfabetoU)):

				if frase[x] == alfabetoU[y]:
					frase[x] = "H"
					a = 1

		if a != 1:
		
			for y in range(0, len(alfabetoC)):

				if frase[x] == alfabetoC[y]:
					frase[x] = "P"
					a = 1				

	#Saida

	frase = "".join(frase)

	print("\n\n Frase: " + frase)

	input("\n\nPressione Enter para continuar")

def ajuda():

	print("um dia escreveremos essa parte do código, abraço")
	
	input("\n\nPressione Enter para continuar")

def sobre():
	print ("Sobre:\n\
		\n\
		Esse programa criptografa usando o ROT13, ou cifra do Kama-Sutra.\n\
		É o desafio de férias número 1 proposto pelo GECA (Grupo de estudos criptográficos de Americana)\n\
	Versão:\n\
		\n\
		0.1 (09/12/2014)\n\
		0.2 (12/12/2014)\n\
		\n\
	Desevolvedores:\n\
		0.1\n\
			Eduardo F. Mendes (z4r4tustr4)	mendesxeduardo@gmail.com\n\
			Jacomo Giovanetti				jacomogiovanettimn@gmail.com\n\
		0.2\n\
			Eduardo F. Mendes (z4r4tustr4)\n\
			Jacomo Giovanetti\n\
		\n\
	Debug:\n\
		0.1\n\
			William G. Lopes (WgL)			williangldzn@gmail.com\n")

	input("\n\nPressione Enter para continuar")

#função do menu inicial do programa
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

	if menu == "1":
		entradaLimpa = input("Digite a frase a ser criptografada: \b")
		entradaLimpa = entradaLimpa.upper()
		frase = list(entradaLimpa)
		cripto(frase)
	elif menu == "2":
		entradaSuja = input("Digite a frase a ser descriptografada: \b")
		entradaSuja = entradaSuja.upper()
		frase = list(entradaSuja)
		cripto(frase)
	elif menu == "3":
		print ("Muito louco caraaaaaaaaaaaaaaaaaaaaa")
	elif menu == "4":
		sobre()
	elif menu == "5":
		exit()

#Úm laço para manter o menu constante
def main():
	while True:
		menu()

main()
