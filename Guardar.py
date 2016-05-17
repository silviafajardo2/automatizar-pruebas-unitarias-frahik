from Mate import media
x = media()
p=-1

def salvar(valores,n="-",proceso="-", resultado=0):
    l = open("Valores.txt", "r")
    numP = len(l.readlines()) + 1

    pruebas = open("Valores.txt", "a")
    if n is "-":
        pruebas.write(str(numP).zfill(4) + ":" + proceso + ":" + str(valores) + ":" + str(resultado) + "\n")
    else:
        pruebas.write(str(numP).zfill(4) + ":" + proceso + ":" + str(valores) +"," +str(n) + ":" + str(resultado) + "\n")
    pruebas.close()

while(p != 0):
    p = int(raw_input("##### Que metodo quieres usar? ##### \n 1:Media Aritmetica \n 2:Raiz Enesima\n 3:Media Geometrica\n 4:Media Armonica\n"))
    if p == 1:
        valores = raw_input("----- Media Aritmetica -----\n Inserta los valores (Separados por coma):\n")
        resultado = x.media_aritmetica(map(int, valores.split(",")))
        salvar(valores=valores,proceso="Media Aritmetica",resultado=resultado)
    elif p == 2:
        valores = int(raw_input("----- Raiz Enesima ----- \n Inserta el valor x:\n"))
        n = int(raw_input("Inserta el valor n:\n"))
        resultado = x.raiz_enesima(valores,n)
        salvar(valores=valores,n=str(n), proceso="Raiz Enesima", resultado=resultado)
    elif p == 3:
        valores = raw_input("----- Media Geometrica -----\n Inserta los valores (Separados por coma):\n")
        resultado = x.media_geometrica(map(int, valores.split(",")))
        salvar(valores=valores, proceso="Media Geometrica", resultado=resultado)
    elif p == 4:
        valores = raw_input("----- Media Armonica -----\n Inserta los valores (Separados por coma):\n")
        try:
            resultado = x.media_armonica(valores)
        except:
            print "Para que le juegas al vergas?"
            resultado = "-"
        salvar(valores=valores, proceso="Media Armonica", resultado="-")
    else:
        print "Finalizado, Creo..."
        resultado = ""

    print resultado

