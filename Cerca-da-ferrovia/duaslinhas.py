mensagem = input("Digite a mensagem:  ").upper().replace(" ","")

saida = ""
x = 0

while x < 2:
	
	saida += mensagem[x::linhas]
	
	x += 1

print(saida)
