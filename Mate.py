class media(object):
    def __init__(self):
        pass

    def media_aritmetica(self,datos =[]):
        return (sum(datos)*1.0)/len(datos)

    def raiz_enesima(self, x, n):
        try:
            return x**(1.0/n)
        except:
            raise Exception(ValueError)

    def media_geometrica(self,datos = []):
        resultado_multiplicacion = 1.0
        for numero in range(len(datos)):
            resultado_multiplicacion = resultado_multiplicacion * datos[numero]
        x = media()
        return x.raiz_enesima(x=resultado_multiplicacion, n=len(datos))

    def media_armonica(self, datos =[]):
        raise Exception("Sin implementar")
