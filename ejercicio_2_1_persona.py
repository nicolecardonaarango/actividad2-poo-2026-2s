class Persona:

    def __init__(self, nombre, apellidos, numero_documento_identidad, año_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.año_nacimiento = año_nacimiento

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.año_nacimiento}")
        print()


def main():
    p1 = Persona("Juan", "Santos", "1043121010", 1997)
    p2 = Persona("John", "Smith", "1053278344", 2002)
    p1.imprimir()
    p2.imprimir()


if __name__ == "__main__":
    main()