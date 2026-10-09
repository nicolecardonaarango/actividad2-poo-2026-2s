from enum import Enum

class Planeta:

    class TipoPlaneta(Enum):
        GASEOSO = "GASEOSO"
        TERRESTRE = "TERRESTRE"
        ENANO = "ENANO"

    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro,
                 distancia_sol, tipo, es_observable):
     
        self.nombre = None               
        self.cantidad_satelites = 0      
        self.masa = 0.0                  
        self.volumen = 0.0               
        self.diametro = 0               
        self.distancia_sol = 0           
        self.tipo = None                 
        self.es_observable = False       
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        
        limite = 149597870 * 3.4
        
        if self.distancia_sol > limite:
            return True
        else:
            return False

    @staticmethod
    def main():
       
        p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742,
                     150000000, Planeta.TipoPlaneta.TERRESTRE, True)
        p1.imprimir()
        print(f"Densidad del planeta = {p1.calcular_densidad()}")
        print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
        print()
        p2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820,
                     750000000, Planeta.TipoPlaneta.GASEOSO, True)
        p2.imprimir()
        print(f"Densidad del planeta = {p2.calcular_densidad()}")
        print(f"Es planeta exterior = {p2.es_planeta_exterior()}")

if __name__ == "__main__":
    Planeta.main()
    