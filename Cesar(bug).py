#!/bin/python3.4

#imports

import os, signal

#Função que executa a Cifra de cesar
def cripto(entrada,b):
	
	if b == "0":
	
		entrada = entrada.replace("W","Z")
		entrada = entrada.replace("X","Y")
		entrada = entrada.replace("V","W")
		entrada = entrada.replace("U","X")
		entrada = entrada.replace("T","V")
		entrada = entrada.replace("S","U")
		entrada = entrada.replace("R","T")
		entrada = entrada.replace("Q","S")
		entrada = entrada.replace("P","R")
		entrada = entrada.replace("O","Q")
		entrada = entrada.replace("N","P")
		entrada = entrada.replace("M","O")
		entrada = entrada.replace("L","N")
		entrada = entrada.replace("K","M")
		entrada = entrada.replace("J","L")
		entrada = entrada.replace("I","K")
		entrada = entrada.replace("H","J")
		entrada = entrada.replace("G","I")
		entrada = entrada.replace("F","H")
		entrada = entrada.replace("E","G")
		entrada = entrada.replace("D","F")
		entrada = entrada.replace("C","E")
		entrada = entrada.replace("B","D")
		entrada = entrada.replace("A","C")
		entrada = entrada.replace("Y","A")
		entrada = entrada.replace("Z","B")
	
	if b == "1":
	
		entrada = entrada.replace("C","A")
		entrada = entrada.replace("D","B")
		entrada = entrada.replace("E","C")
		entrada = entrada.replace("F","D")
		entrada = entrada.replace("G","E")
		entrada = entrada.replace("H","F")
		entrada = entrada.replace("I","G")
		entrada = entrada.replace("J","H")
		entrada = entrada.replace("K","I")
		entrada = entrada.replace("L","J")
		entrada = entrada.replace("M","K")
		entrada = entrada.replace("N","L")
		entrada = entrada.replace("O","M")
		entrada = entrada.replace("P","N")
		entrada = entrada.replace("Q","O")
		entrada = entrada.replace("R","P")
		entrada = entrada.replace("S","Q")
		entrada = entrada.replace("T","R")
		entrada = entrada.replace("U","S")
		entrada = entrada.replace("V","T")
		entrada = entrada.replace("X","U")
		entrada = entrada.replace("Y","V")
		entrada = entrada.replace("Z","X")
		entrada = entrada.replace("A","Y")
		entrada = entrada.replace("B","Z")

	#Saida

	print("\n\n Frase: " + entrada)

	input("\n\nPressione Enter para continuar")

#função do menu inicial do programa
def menu():
	#Menu inicial
	os.system('clear')

	print("	=== Menu ===\n\
	1. Criptografar\n\
	2. Descriptografar\n\
	")

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
