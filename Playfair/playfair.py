#!/usr/bin/env python3

def cripto(frase, chave, chaveador):
	
	#Importa a matriz montada
	matriz = monta_matriz(chave)
	
	posicao = 0
	texto_cifrado = ""
	
	#Ajuste caso a frase tenha uma quantidade impar de caracteres
	if len(frase) % 2:
		frase += "x"
		
	#Validação no caso de duas letras iguais
	if frase[posicao] is frase[posicao+1]:
		frase[posicao+1] = "x"
	
	while posicao < len(frase):

		#Parte onde as duas letras correm a matriz
		posicao_m = 0
		for linha in matriz:
			for coluna in linha:
				if coluna is frase[posicao]:
					letra_1_l = posicao_m // 5
					letra_1_c = posicao_m % 5
				posicao_m += 1

		posicao_m = 0
		for linha in matriz:
			for coluna in linha:
				if coluna is frase[posicao+1]:
					letra_2_l = posicao_m // 5
					letra_2_c = posicao_m % 5
				posicao_m += 1

		#Shift +1 de Colunas
		if letra_1_l is letra_2_l:
			
			if chaveador is "1":
				letra_1_c = (letra_1_c + 1) % 5 
				letra_2_c = (letra_2_c + 1) % 5
			else:
				letra_1_c = (letra_1_c - 1) % 5 
				letra_2_c = (letra_2_c - 1) % 5

			texto_cifrado += matriz[letra_1_l][letra_1_c]+matriz[letra_2_l][letra_2_c]
		
		#Shift +1 de Linhas
		elif letra_1_c is letra_2_c:
			if chaveador is "1":
				letra_1_l = (letra_1_l + 1) % 5
				letra_2_l = (letra_2_l + 1) % 5
			else:
				letra_1_l = (letra_1_l - 1) % 5
				letra_2_l = (letra_2_l - 1) % 5

			texto_cifrado += matriz[letra_1_l][letra_1_c]+matriz[letra_2_l][letra_2_c]

		#Shift N(C)
		elif (letra_1_l != letra_2_l) and (letra_1_c != letra_2_c):
			
			letra_2_c_r = letra_1_c
			letra_1_c_r = letra_2_c

			texto_cifrado += matriz[letra_1_l][letra_1_c_r]+matriz[letra_2_l][letra_2_c_r]


		posicao += 2

	#Um print da matriz completa para executar testes manuais, caso haja erro
	print("",matriz[0],"\n",matriz[1],"\n",matriz[2],"\n",matriz[3],"\n",matriz[4])

	#Exibe a resposta
	print(texto_cifrado)

	input("Precione enter para continuar...")

def monta_matriz(chave):
	alfabeto = list("abcdefghiklmnopqrstuvwxyz")

	matriz = [[0,0,0,0,0],
			  [0,0,0,0,0],
			  [0,0,0,0,0],
			  [0,0,0,0,0],
			  [0,0,0,0,0]]

	linha = 0
	coluna = 0
	posicao = 0

	for letra in chave:

		#Indica a posição na matriz usando AM.
		linha = int(posicao / 5)	#Na primeira [0] -> [1] ..... [5]
		coluna = int(posicao % 5)	#Na primeira [0] -> [0] ..... [5]

		if letra in alfabeto:
			#Remove as letras do alfabeto e insere a chave + alfabeto na matriz
			alfabeto.remove(letra)
			matriz[linha][coluna] = letra
			posicao += 1

	#Insersão dos caracteres restantes no alfabeto
	while (len(alfabeto) > 0):
		
		linha = int(posicao / 5)
		coluna = int(posicao % 5)
		matriz[linha][coluna] = alfabeto.pop(0)
		
		posicao += 1

	return(matriz)
