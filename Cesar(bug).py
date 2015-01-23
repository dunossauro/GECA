#!/bin/python3.4

#imports

import os, signal

#Função que executa a Cifra de cesar
def cripto(entrada,b):
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
