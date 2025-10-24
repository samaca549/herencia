class Animales:
    def __init__(self, edad, reproduccion, especie):
        self.edad = edad
        self.reproduccion = reproduccion
        self.especie = especie

    def presentarse(self):
        return f"Su animal tiene {self.edad} años, su tipo de reproducción es {self.reproduccion}, y su especie es {self.especie}."
    
    def to_dict(self):

        return {
            "edad": self.edad,
            "reproduccion": self.reproduccion,
            "especie": self.especie
        }


class Mamiferos(Animales):
    def __init__(self, edad, reproduccion, especie, habitat, condicion):
        super().__init__(edad, reproduccion, especie)
        self.habitat = habitat
        self.condicion = condicion

    def mostrar_caracteristicas(self):
        return f"Su animal vive en {self.habitat}, y su estado es {self.condicion}."

    def to_dict(self):
      
        data = super().to_dict()
        data.update({
            "habitat": self.habitat,
            "condicion": self.condicion
        })
        return data


class Ornitorrinco(Mamiferos):
    def __init__(self, edad, reproduccion, especie, habitat, condicion, genero, alimentos, estado_de_animo, nombre):
        super().__init__(edad, reproduccion, especie, habitat, condicion)
        self.genero = genero
        self.alimentos = alimentos
        self.estado = estado_de_animo
        self.nombre = nombre

    def poner_huevos(self):
        if self.genero.lower() == "hembra":
            return f"El ornitorrinco {self.nombre} es hembra, puede poner huevos y tiene {self.edad} años."
        else:
            return f"El ornitorrinco {self.nombre} es macho, no puede poner huevos."

    def veneno_defensa(self):
        if self.genero.lower() == "macho":
            return f"El ornitorrinco {self.nombre} está en estado de {self.estado} y usará su espolón venenoso para defenderse."
        else:
            return f"El ornitorrinco {self.nombre} es hembra y no posee espolón venenoso."

    def detectar_alimento(self):
        return f"El ornitorrinco {self.nombre} detecta impulsos eléctricos bajo el agua para cazar {self.alimentos}. USTED LE DIO EL PERMISO DE CAZAR"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "genero": self.genero,
            "alimentos": self.alimentos,
            "estado_de_animo": self.estado
        })
        return data


class Canguro(Mamiferos):
    def __init__(self, edad, reproduccion, especie, habitat, condicion, genero, nombre):
        super().__init__(edad, reproduccion, especie, habitat, condicion)
        self.genero = genero
        self.nombre = nombre

    def saltar(self):
        return f"El canguro {self.nombre} está saltando con sus patas traseras poderosas."

    def usar_marsupio(self):
        if self.genero.lower() == "hembra":
            return f"La canguro {self.nombre} puede llevar a su cría en el marsupio."
        else:
            return f"El canguro {self.nombre} no tiene marsupio, es macho."

    def comportamiento_social(self):
        return f"El canguro {self.nombre} vive en grupos llamados 'mobs' y es de género {self.genero}."

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "genero": self.genero
        })
        return data


class Elefante(Mamiferos):
    def __init__(self, edad, reproduccion, especie, habitat, condicion, genero, nombre, tamaño_colmillos, memoria):
        super().__init__(edad, reproduccion, especie, habitat, condicion)
        self.genero = genero
        self.nombre = nombre
        self.tamaño_colmillos = tamaño_colmillos
        self.memoria = memoria

    def usar_trompa(self):
        return f"El elefante {self.nombre} usa su trompa para beber agua, alimentarse y comunicarse."

    def mostrar_colmillos(self):
        return f"El elefante {self.nombre} tiene colmillos de {self.tamaño_colmillos} cm de largo. y ahora esta sonriendo porque esta orgulloso de sus colmillos"

    def recordar_rutas(self):
        if self.memoria:
            return f"El elefante {self.nombre} tiene excelente memoria y recuerda rutas migratorias complejas."
        else:
            return f"El elefante {self.nombre} tiene memoria limitada."
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "genero": self.genero,
            "tamaño_colmillos_cm": self.tamaño_colmillos,
            "tiene_buena_memoria": self.memoria
        })
        return data