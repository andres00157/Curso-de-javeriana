print ("recuerde que el valor minimo de ingreso es de 200$ y el valor maximo de 2500$")
print ("solo se aceptan monedas")
print ("ingrese su dinero")
a = int(raw_input("cuantas monedas de 100$"))
b = int(raw_input("cuantas monedas de 200$"))
c = int(raw_input("cuantas monedas de 500$"))
d = ( a * 100 )
e = ( b * 200 )
f = ( c * 500 )
g = (d + e + f)
if g < 2600:
    if g > 100:
     print (g ,"pesos tienes acumulados")
     print ("en que losquieres gastas")
     print  ("1 Papas Fritas $1200")
     print ("2 sandwich combinado $2500")
     print ("3 Pescadito $1800")
     print ("4 Empanada $1700")
     print ("5 Arepa $2000")
     print ("6 Gaseosa $1600")
     print ("7 Vaso de te $1000")
     print ("8 Dulce $200")
     print ("9 Salir")
     h = int(raw_input("numero de producto"))
     print h
     if h == 1:
        if g < 1100:
         print ("lo lamento pero no te alcanza la plata")
         i = (g / 500)
         o = (g % 500)
         p = (o / 200)
         q = (o % 200)
         r = (q / 100)
         print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
         print ("se le devuelve"), g,  ("pesos")
        if g >= 1200:
            print ("elegiste las papas fritas")
            print ("toma las papas fritas")
            y = (g - 1200)
            i = (y / 500)
            o = (y % 500)
            p = (o / 200)
            q = (o % 200)
            r = (q / 100)
            print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
            print ("cambio de =") , y
     if h == 2:
         if g < 2500:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 2500:
             print ("elegiste las sandwich conbinado")
             print ("toma el sandwich conbinado")
             y = (g - 2500)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y
     if h == 3:
         if g < 1800:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 1800:
             print ("elegiste el pescadito")
             print ("toma el pescadito")
             y = (g - 1800)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y
     if h == 4:
         if g < 1700:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 1700:
             print ("elegiste la empanada")
             print ("toma la empanada")
             y = (g - 1700)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y
     if h == 5:
         if g < 2000:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 2000:
             print ("elegiste la arepa")
             print ("toma la arepa")
             y = (g - 2000)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y
     if h == 6:
         if g < 1600:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 1600:
             print ("elegiste la gaseosa")
             print ("toma la gaseosa")
             y = (g - 1600)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y             
     if h == 7:
         if g < 1000:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 1000:
             print ("elegiste el vaso de te")
             print ("toma el vaso de te")
             y = (g - 1000)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y         
     if h == 8:
         if g < 200:
             print ("lo lamento pero no te alcanza la plata")
             i = (g / 500)
             o = (g % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("se le devuelve"), g,  ("pesos")
         if g >= 200:
             print ("elejiste el dulce")
             print ("toma el dulce")
             y = (g - 200)
             i = (y / 500)
             o = (y % 500)
             p = (o / 200)
             q = (o % 200)
             r = (q / 100)
             print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
             print ("cambio de =") , y
     if h == 9:
         print ("se reembolsara la plata que metiste")
         i = (g / 500)
         o = (g % 500)
         p = (o / 200)
         q = (o % 200)
         r = (q / 100)
         print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
         print ("se le devuelve"), g,  ("pesos")           
print ("lo lamento pero no puedes comprar nada en esta maquina")
print ("se reembolsara la plata que metiste")
i = (g / 500)
o = (g % 500)
p = (o / 200)
q = (o % 200)
r = (q / 100)
print ("monedas de 500="), i, ("monedas de 200="), p, ("monedas de 100="), r
print ("se le devuelve"), g,  ("pesos")
    
