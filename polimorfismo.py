class Armas:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def hacer_sonido(self):
        return"sonido generico"
class Pistola(Armas):
    def hacer_sonido(self):
        return "Piu, Piu"
    
class Granada(Armas):
    def hacer_sonido(self):
        return "Boom"

class Cuchillo(Armas):
    def hacer_sonido(self):
        return "Crac, Crac"
    
def imprimir_sonido(arma):
    print(arma.hacer_sonido())
    
pistola= Pistola("Thunderstrike", 2)
granada= Granada("RPG-7:", 5)
cuchillo= Cuchillo("M6 Bayonet", 3)

imprimir_sonido(pistola)
imprimir_sonido(granada)
imprimir_sonido(cuchillo)