lista1 = []
print "quieres agragar un numero"
r = raw_input("respuesta=")
while r == "si" :
    a =int(raw_input("numero"))
    lista1.append (a)
    r = raw_input("respuesta=")
   
print lista1
p =len(lista1)
mayor = 0
for i in range (p):
   if lista1[i] > mayor:
       mayor = lista1[i]
print mayor
