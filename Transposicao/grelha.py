mensagem = input("Digite a mensagem:  ").upper().replace(" ","")
linhas = int(input("Digite o numero de linhas:  "))
saida
 = ""
x = 0

while x < linhas:
	
	saida += mensagem[x::linhas]
	
	x += 1

print(saida)
