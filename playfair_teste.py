chave = input("digite a chave: \n")
mensagem = input("digite a mensagem: \n")


#######		matriz	####
alfabeto = list("abcdefghiklmnopqrstuvwxyz")

matriz = [[0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0]]

linha = 0
coluna = 0
posicao = 0

#Insersão da chave na matriz
for letra in chave:

	#Indica a posição na matriz usando AM.
	linha = int(posicao / 5)	#Na primeira [0] -> [1] ..... [5]
	coluna = int(posicao % 5)	#Na primeira [0] -> [0] ..... [1]

	if letra in alfabeto:
		#Remove as letras do alfabeto e insere a chave + alfabeto na matriz
		alfabeto.remove(letra)
		matriz[linha][coluna] = letra
		posicao += 1

#Insersão dos caracteres restantes no alfabeto
while(len(alfabeto) > 0):
	
	linha = int(posicao / 5)
	coluna = int(posicao % 5)
	matriz[linha][coluna] = alfabeto.pop(0)
	
	posicao += 1
#print(matriz)

################	mensagem	#########

posicao = 0
texto_cifrado = ""

while posicao < len(mensagem):
	
	letra_1 = mensagem[posicao]
	letra_2 = mensagem[posicao+1]
	
	posicao_m = 0
	for linha in matriz:
		for coluna in linha:
			if coluna is letra_1:
				letra_1_l = posicao_m//5
				letra_1_c = posicao_m%5
			posicao_m += 1

	posicao_m = 0
	for linha in matriz:
		for coluna in linha:
			if coluna is letra_2:
				letra_2_l = posicao_m//5
				letra_2_c = posicao_m%5
			posicao_m += 1

	if letra_1_l is letra_2_l:
		letra_1_c = (letra_1_c + 1)%5 
		letra_2_c = (letra_2_c + 1)%5
	
	elif letra_1_c is letra_2_c:
		letra_1_l = (letra_1_l + 1)%5
		letra_2_l = (letra_2_l + 1)%5

	elif (letra_1_l != letra_2_l) and (letra_1_c != letra_2_c):
		
		letra_2_c_r = letra_1_c
		letra_1_c_r = letra_2_c

	letra_1 = matriz[letra_1_l][letra_1_c_r]
	letra_2 = matriz[letra_2_l][letra_2_c_r]

	texto_cifrado += letra_1+letra_2


	posicao += 2

print("",matriz[0],"\n",matriz[1],"\n",matriz[2],"\n",matriz[3],"\n",matriz[4])

print(texto_cifrado)
