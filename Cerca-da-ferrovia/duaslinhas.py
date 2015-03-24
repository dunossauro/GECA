#!/usr/bin/python 3

mensagem = input("Digite a mensagem:  ").upper().replace(" ","")
linha1 = ""
linha2 = ""
saida = ""

#"Tratamento"
if len(mensagem) % 2 is 1:
	mensagem += " "

#criptografar
for x in range(len(mensagem)):

	if x % 2 is 0:
		linha1 += mensagem[x]
	else:
		linha2 += mensagem[x]

print("%s%s" % (linha1,linha2))

#Decriptografar
for x in range(len(linha1)):
	
	saida += linha1[x]
	saida += linha2[x]

print(saida)
