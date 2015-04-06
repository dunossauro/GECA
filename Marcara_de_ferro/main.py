
from random import shuffle

chaveador = '1'
#Definição de listas (Não precisa ser assim, mas quero ser visível)
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []

def _gen(arq):

	arquivo = open(arq,'r')

	for x in arquivo:
		yield x.strip()

def _map(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
	
	#Fase das atribuições dos valores
	cont = 0
	for _x in _gen('Mascara_Beale.txt'):
		for y in _x:
			if y == 'a':
				a.append(cont)
			if y == 'b':
				b.append(cont)
			if y == 'c':
				c.append(cont)
			if y == 'd':
				d.append(cont)
			if y == 'e':
				e.append(cont)		
			if y == 'f':
				f.append(cont)
			if y == 'g':
				g.append(cont)
			if y == 'h':
				h.append(cont)
			if y == 'i':
				i.append(cont)
			if y == 'j':
				j.append(cont)
			if y == 'k':
				k.append(cont)
			if y == 'l':
				l.append(cont)
			if y == 'm':
				m.append(cont)
			if y == 'n':
				n.append(cont)
			if y == 'o':
				o.append(cont)
			if y == 'p':
				p.append(cont)
			if y == 'q':
				q.append(cont)
			if y == 'r':
				r.append(cont)
			if y == 's':
				s.append(cont)
			if y == 't':
				t.append(cont)
			if y == 'u':
				u.append(cont)
			if y == 'v':
				v.append(cont)
			if y == 'x':
				x.append(cont)
			if y == 'w':
				w.append(cont)
			if y == 'y':
				y.append(cont)
			if y == 'z':
				z.append(cont)
			cont += 1

def _cripto(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
	saida = []
	for _x in _gen('texto.txt'):
		for y in _x:
			if y == 'a':
				shuffle(a)
				saida.append(a[0])
			if y == 'b':
				shuffle(b)
				saida.append(b[0])
			if y == 'c':
				shuffle(c)
				saida.append(c[0])
			if y == 'd':
				shuffle(d)
				saida.append(d[0])
			if y == 'e':
				shuffle(e)
				saida.append(e[0])
			if y == 'f':
				shuffle(f)
				saida.append(f[0])
			if y == 'g':
				shuffle(g)
				saida.append(g[0])
			if y == 'h':
				shuffle(h)
				saida.append(h[0])
			if y == 'i':
				shuffle(i)
				saida.append(i[0])
			if y == 'j':
				shuffle(j)
				saida.append(j[0])
			if y == 'k':
				shuffle(k)
				saida.append(k[0])
			if y == 'l':
				shuffle(l)
				saida.append(l[0])
			if y == 'm':
				shuffle(m)
				saida.append(m[0])
			if y == 'n':
				shuffle(n)
				saida.append(n[0])
			if y == 'o':
				shuffle(o)
				saida.append(o[0])
			if y == 'p':
				shuffle(p)
				saida.append(p[0])
			if y == 'q':
				shuffle(q)
				saida.append(q[0])
			if y == 'r':
				shuffle(r)
				saida.append(r[0])
			if y == 's':
				shuffle(s)
				saida.append(s[0])
			if y == 't':
				shuffle(t)
				saida.append(t[0])
			if y == 'u':
				shuffle(u)
				saida.append(u[0])
			if y == 'v':
				shuffle(v)
				saida.append(v[0])
			if y == 'w':
				shuffle(w)
				saida.append(w[0])
			if y == 'x':
				shuffle(x)
				saida.append(x[0])
			if y == 'y':
				shuffle(y)
				saida.append(y[0])
			if y == 'z':
				shuffle(z)
				saida.append(z[0])
	
	f = open('saida.txt','w')
	f.write(str(saida))

def _decripto(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z): pass 

#chamadas
_map(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)

#cripto ou decripto?
if chaveador is '1':
	saida = _cripto(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
else:
	saida = _decripto(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
