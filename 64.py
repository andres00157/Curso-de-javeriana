

print"cualcular  o  par o impar"
r = (raw_input("elige"))
if r=="calculadora" or r=="Calculadora" or r=="calcular" or r=="CALCULADORA":
    print "calculadora"
    var1 = int(raw_input("escribe un numero"))
    var2 = int(raw_input("escribe un numero"))
    print "elige suma, resta, multiplicacion y  para saber divicion y residuo"
    r2 = (raw_input("elige"))
    if r2== "suma" or r2=="Suma" :
        print "suma", var1 + var2
    if r2 =="resta" or r2=="Resta":
        print "resta", var1 - var2
    if r2 =="multiplicacion" or r2=="Multiplicacion":
        print "multiplicacion", var1 * var2
    if r2 == "division" or r2=="Division":
        if var2!=0:
            print "divisin", var1 /var2
            print "residuo", var1 % var2
        else: print"no se puede"
if r == "par o impar":
    print "par o impar"
    var3 = int(raw_input("elige"))
    
    var4= var3 % 2
    if var4 != 0:
        print"es impar"
    else:print"es par"
    
