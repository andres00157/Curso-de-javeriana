lista1 = []
lista2 = []
print "quieres agragar la edad y el numero"
r = raw_input("respuesta=")
while r == "si" :
    a =int(raw_input("edad"))
    b =(raw_input("nombre"))
    lista1.append (a)
    lista2.append (b)
    r = raw_input("respuesta=")
   
print lista1
print lista2
p =len(lista1)
mayor = 0
y= "posision"
for i in range (p):
   if lista1[i] > mayor:
       mayor = lista1[i]
       y=i
print lista2[y]
print mayor

