from random import shuffle

def zero():

	mat = [
		[],#a
		[],#b
		[],#c
		[],#d
		[],#e
		[],#f
		[],#g
		[],#h
		[],#i
		[],#j
		[],#k
		[],#l
		[],#m
		[],#n
		[],#n
		[],#o
		[],#p
		[],#q
		[],#r
		[],#s
		[],#t
		[],#u
		[],#v
		[],#x
		[],#w
		[],#y
		[],#z
		]
	return(mat)

def gen(arq):
	arquivo = open(arq,'r')

	for x in arquivo:
		yield x.strip()

def map(zero):
	cont = 0
	for _x in gen('Mascara_Beale.txt'):
		for _y in _x:
			if _y is 'a':
				zero[0].append(cont)
			if _y is 'b':
				zero[1].append(cont)
			if _y is 'c':
				zero[2].append(cont)
			if _y is 'd':
				zero[3].append(cont)
			if _y is 'e':
				zero[4].append(cont)
			if _y is 'f':
				zero[5].append(cont)
			if _y is 'g':
				zero[6].append(cont)
			if _y is 'h':
				zero[7].append(cont)
			if _y is 'i':
				zero[8].append(cont)
			if _y is 'j':
				zero[9].append(cont)
			if _y is 'k':
				zero[10].append(cont)
			if _y is 'l':
				zero[11].append(cont)
			if _y is 'm':
				zero[12].append(cont)
			if _y is 'n':
				zero[13].append(cont)
			if _y is 'n':
				zero[14].append(cont)
			if _y is 'o':
				zero[15].append(cont)
			if _y is 'p':
				zero[16].append(cont)
			if _y is 'q':
				zero[17].append(cont)
			if _y is 'r':
				zero[18].append(cont)
			if _y is 's':
				zero[19].append(cont)
			if _y is 't':
				zero[20].append(cont)
			if _y is 'u':
				zero[21].append(cont)
			if _y is 'v':
				zero[22].append(cont)
			if _y is 'x':
				zero[23].append(cont)
			if _y is 'w':
				zero[24].append(cont)
			if _y is 'y':
				zero[25].append(cont)
			if _y is 'z':
				zero[26].append(cont)
			cont += 1
	return(zero)

def cripto(_map):
	saida = []
	for _x in gen('texto.txt'):
		for y in _x:
			if y == 'a':
				shuffle(map[0])
				saida.append(map[0][0])
			if y == 'b':
				shuffle(map[1])
				saida.append(map[1][0])
			if y == 'c':
				shuffle(map[2])
				saida.append(map[2][0])
			if y == 'd':
				shuffle(map[3])
				saida.append(map[3][0])
			if y == 'e':
				shuffle(map[4])
				saida.append(map[4][0])
			if y == 'f':
				shuffle(map[5])
				saida.append(map[5][0])
			if y == 'g':
				shuffle(map[6])
				saida.append(map[6][0])
			if y == 'h':
				shuffle(map[7])
				saida.append(map[7][0])
			if y == 'i':
				shuffle(map[8])
				saida.append(map[8][0])
			if y == 'j':
				shuffle(map[9])
				saida.append(map[9][0])
			if y == 'k':
				shuffle(map[10])
				saida.append(map[10][0])
			if y == 'l':
				shuffle(map[11])
				saida.append(map[11][0])
			if y == 'm':
				shuffle(map[12])
				saida.append(map[12][0])
			if y == 'n':
				shuffle(map[13])
				saida.append(map[13][0])
			if y == 'o':
				shuffle(map[14])
				saida.append(map[14][0])
			if y == 'p':
				shuffle(map[15])
				saida.append(map[15][0])
			if y == 'q':
				shuffle(map[16])
				saida.append(map[16][0])
			if y == 'r':
				shuffle(map[17])
				saida.append(map[17][0])
			if y == 's':
				shuffle(map[18])
				saida.append(map[18][0])
			if y == 't':
				shuffle(map[19])
				saida.append(map[19][0])
			if y == 'u':
				shuffle(map[20])
				saida.append(map[20][0])
			if y == 'v':
				shuffle(map[21])
				saida.append(map[21][0])
			if y == 'w':
				shuffle(map[22])
				saida.append(map[22][0])
			if y == 'x':
				shuffle(map[23])
				saida.append(map[23][0])
			if y == 'y':
				shuffle(map[24])
				saida.append(map[24][0])
			if y == 'z':
				shuffle(map[25])
				saida.append(map[25][0])
	return(saida)
	print(saida)

def decripto(map):
	saida = []
	for _x in gen('saida.txt'):
			print(_x)
			if _x in map[0]:
				saida.append('a')
			if _x in map[1]:
				saida.append('b')
			if _x in map[2]:
				saida.append('c')
			if _x in map[3]:
				saida.append('d')
			if _x in map[4]:
				saida.append('e')
			if _x in map[5]:
				saida.append('f')
			if _x in map[6]:
				saida.append('g')
			if _x in map[7]:
				saida.append('h')
			if _x in map[8]:
				saida.append('i')
			if _x in map[9]:
				saida.append('j')
			if _x in map[10]:
				saida.append('k')
			if _x in map[11]:
				saida.append('l')
			if _x in map[12]:
				saida.append('m')
			if _x in map[13]:
				saida.append('n')
			if _x in map[14]:
				saida.append('o')
			if _x in map[15]:
				saida.append('p')
			if _x in map[16]:
				saida.append('q')
			if _x in map[17]:
				saida.append('r')
			if _x in map[18]:
				saida.append('s')
			if _x in map[19]:
				saida.append('t')
			if _x in map[20]:
				saida.append('u')
			if _x in map[21]:
				saida.append('v')
			if _x in map[22]:
				saida.append('w')
			if _x in map[23]:
				saida.append('x')
			if _x in map[24]:
				saida.append('y')
			if _x in map[25]:
				saida.append('z')
	return(saida)

def main ():
	
	chaveador = '1'
	
	_zero = zero()
	_map = map(_zero)
	if chaveador is '1':
		_cripto = cripto(_map)
	else:
		_decripto = decripto(_map)

main()
