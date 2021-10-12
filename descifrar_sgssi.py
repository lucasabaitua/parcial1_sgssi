#creamos una función para que nos indique si hay un elemento 'x' en una lista
def esta(x, lista):
        for i in lista: 
                if i==x:
                        return True
                               
#creamos una función que intercambie los valores de una funcion con ayuda de una variable auxiliar
def cambiar(A, x, y):
    aux = A[x]
    A[x] = A[y]
    A[y] = aux

#creamos una funcion que vaya recorriendo una lista y vaya ordenando los elementos de mayor a menor 
def ordenarMayor(l):
    for i in range(len(l)):
        act = i
        for j in range(i+1, len(l)):
            if l[j] > l[act]:
                act = j
                 
        cambiar(l, act, i)


mensaje ='''RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE 
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ 
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX 
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, 
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN 
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, 
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK 
HKCZJOI OKEJSZCNHE.'''
max=0
letra=' '
lista=[]
nueva=[]
#contamos los caracteres que mas se repiten y los almacenamos en orden de más veces a menos veces
for i in mensaje:
	cont=0
	j=i
	
	for j in mensaje:
		#no contamos los caracteres especiales
		if i==j and (j!=' ' and  j!='.' and  j!=',' and j!='·' and j!='\n'):
				cont=cont+1
	
	if not  esta(cont, nueva):
		
		nueva.append(cont)
	if max<cont:
		max=cont
		letra=i
ordenarMayor(nueva)

#contamos las veces que los caracteres que mas se repiten en la cadena del mensaje aparecen de mayor a menor
for i in  nueva: 
	
	for j in mensaje : 
		cont=0
		k=j
		for k in mensaje:
			if j==k and (k!=' ' and  k!='.' and  k!=',' and k!='·' and k!='d'and k!='\n'):
                                cont=cont+1
		if i == cont and not esta(j,lista):
			lista.append(j)

print ("\nCaracteres que aparecen en el mensaje de más veces a menos: ")
print (lista) 
print("\n")
print ("Nº de veces que aparecen: ")
print (nueva)
print ("\n")

print("Los intercambiamos por los que más aparecen en el alfabeto español en orden decreciente y obtenemos el mensaje \n")

#intercambiamos los caracteres que más salen en el mensaje cifrado por los que más salen en el alfabeto español en orden decreciente
#cambiamos a minúsculas para que no haya ningún problema de cambiar letras ya cambiadas
for n in mensaje:
	if n==letra:
		mensaje=mensaje.replace(n,"e")
	if n==lista[1]:
		mensaje=mensaje.replace(n,"a")
	if n=="A":
		mensaje=mensaje.replace(n,"d")
	if n=="T":
		mensaje=mensaje.replace(n,"l")
	if n=="J":
		mensaje=mensaje.replace(n,"n")
	if n=="I":
		mensaje=mensaje.replace(n,"o")
	if n=="D":
		mensaje=mensaje.replace(n,"p")
	if n=="C":
		mensaje=mensaje.replace(n,"i")
	if n=="P":
		mensaje=mensaje.replace(n,"m")
	if n=="Q":
                mensaje=mensaje.replace(n,"b")
	if n=="K":
                mensaje=mensaje.replace(n,"r")
	if n=="R":
                mensaje=mensaje.replace(n,"c")
	if n=="U":
                mensaje=mensaje.replace(n,"g")
	if n=="Z":
                mensaje=mensaje.replace(n,"u")
	if n=="N":
                mensaje=mensaje.replace(n,"s")
	if n=="O":
                mensaje=mensaje.replace(n,"f")
	if n=="H":
                mensaje=mensaje.replace(n,"t")
	if n=="S":
                mensaje=mensaje.replace(n,"q")
	if n=="V":
                mensaje=mensaje.replace(n,"y")
	if n=="F":
                mensaje=mensaje.replace(n,"x")
	if n=="G":
                mensaje=mensaje.replace(n,"j")
	if n=="M":
                mensaje=mensaje.replace(n,"h")
	if n=="L":
                mensaje=mensaje.replace(n,"z")
print ("El mensaje desencriptado es : \n")
print (mensaje + "\n")



