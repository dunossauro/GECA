mensagem = input("Digite a mensagem:  ").upper().replace(" ","")
chaveador = int(input("1 Para criptografar, 2 para descriptografar:  "))
linha = 2
saida = ""

#Tratamento
while len(mensagem) % linha is not 0: mensagem += "_"
coluna = len(mensagem)//linha

if chaveador is 1:
	n_loop = linha
else:
	n_loop = coluna

#Cripto
contador = 0
while contador <  n_loop:
	
	saida += mensagem[contador::n_loop]
	
	contador += 1
print(saida)
