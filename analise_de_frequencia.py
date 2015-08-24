import sys

_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,
    "f":0,"g":0,"h":0,"i":0,"j":0,
    "k":0,"l":0,"m":0,"n":0,"o":0,
    "p":0,"q":0,"r":0,"s":0,"t":0,
    "u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

entrada = input("Digite a frase a ser analisada: \n")

for x in entrada:
    linha = x.strip()

    for x in linha:
        for y in _dict:
            if x == y:
                _dict[x] += 1

for x in sorted(_dict):
    print(x,_dict[x])
