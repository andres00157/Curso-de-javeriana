print "dame los datos de popularidad del primer sia de encuestas"
b = int(raw_input("popularidad="))
if  0<= b <= 101:
    lista1 = [b]
    lista = []
    n = 2
    while 2<= n <= 30:
        print "quieres agragar un numero"
        print "dia" , n
        r = raw_input("respuesta=")
        if r == "si" :
            n = n + 1
            a = int(raw_input("popularidad="))
    
            if 0<= a <= 101:
                lista1.append (a)
                lista.append (n)
            else :
                print"lo lamento pero estos datos estan fuera de los parametros, asi que se haran los calculos con los numeros que tengan"
                break
            
            
            
        else :
           break
    print lista1
    p =len(lista1)
    m = 0
    
    mayor = 0
    for i in range (p):
        if lista1[i] > mayor:
            mayor = lista1[i]
            if i > m:
                m = i
            
    print "dia en el que mayor a tenido popularidad"
    
    print "dia=" ,m  + 1 , "con" , mayor , "puntos  de popularidad"
    print mayor
    if mayor == lista1[0]:
        print"bajando popularidad"
    
else    :
    print"lo lamento pero estos datos estan fuera de los para metros"    

