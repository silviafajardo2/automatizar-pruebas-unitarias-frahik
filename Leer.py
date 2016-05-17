from Mate import media
pruebas = open("valores.txt", "r")
x = media()

for line in pruebas:
    caso = line.split(":")[0]
    p = line.split(":")[1]
    valores = line.split(":")[2]
    resultadoCom = line.split(":")[3]
    try:
        if p == "Media Aritmetica":
            resultado = x.media_aritmetica(map(int, valores.split(",")))
            if resultado == resultadoCom:
                print caso + "\t Exito \t" + ""
        elif p == "Raiz Enesima":
            valores = int(raw_input("----- Raiz Enesima ----- \n Inserta el valor x:\n"))
            n = int(raw_input("Inserta el valor n:\n"))
            resultado = x.raiz_enesima(valores, n)
        elif p == "Media Geometrica":
            valores = raw_input("----- Media Geometrica -----\n Inserta los valores (Separados por coma):\n")
            resultado = x.media_geometrica(map(int, valores.split(",")))
        elif p == "Media Armonica":
            valores = raw_input("----- Media Armonica -----\n Inserta los valores (Separados por coma):\n")
            try:
                resultado = x.media_armonica(valores)
            except:
                print "Para que le juegas al vergas?"
                resultado = "-"
    except:
        print "Errores en el caso: " + caso
#resultados = pruebas.readlines()
#print resultados