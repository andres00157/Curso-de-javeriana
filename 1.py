

i = int(raw_input("i"))
esprimo = (" verdadero")
for t in range(2, i):
    
    
    p = i % t
    if (p)== 0 :
        print ("verdadero")
        print ("no es primo")
        esprimo = ("verdadero")
    else :
        print("falso")
        esprimo = ("falso")

