mensagem = input("Digite a mensagem:  ").upper().replace(" ","")
chaveador = input("1 Para criptografar, 2 para descriptografar:  ")

saida = ""
rodada = ""
x = 0

while x < 2:
	
	if chaveador is "1":
		saida += mensagem[x::2]
	else:
		rodada += mensagem[x::2]
	x += 1

if chaveador is not "1":
	x = 0
	while x < 2:

		saida += rodada[x::2]
		x += 1

print(saida)
