from model.domain import Animales, Canguro, Elefante, Ornitorrinco
from model.data import FirebaseRealtimeService  # O como se llame tu archivo de firebase

class Animales_View_model:
    def __init__(
        self, 
        db_service: FirebaseRealtimeService,
        info_Gene: Animales, 
        Animal1: Ornitorrinco, 
        Animal2: Canguro, 
        Animal3: Elefante
    ):
        self.db = db_service
        self.Animal_gene = info_Gene
        self.orni = Animal1
        self.cang = Animal2
        self.elef = Animal3


    def alimentar_orni(self):
        return self.orni.detectar_alimento()
    

    def defender_orni(self):
        return self.orni.veneno_defensa()
        

    def poner_huevos_orni(self):
        return self.orni.poner_huevos()


    def saltar_cang(self):
        return self.cang.saltar()
        

    def revisar_marsupio_cang(self):
        return self.cang.usar_marsupio()
        

    def ver_social_cang(self):
        return self.cang.comportamiento_social()


    def usar_trompa_elef(self):
        return self.elef.usar_trompa()

    def mostrar_colmillos_elef(self):
        return self.elef.mostrar_colmillos()

    def recordar_rutas_elef(self):
        return self.elef.recordar_rutas()

    def guardar_animales_en_firebase(self):
        print("\n---  GUARDANDO ANIMALES EN FIREBASE (RTDB) ---")
        try:
            key_orni = f"ornitorrincos/{self.orni.nombre}"
            self.db.create(key_orni, self.orni.to_dict())
            print(f"  -> Datos guardados en RTDB (ruta: /{self.db.base_path}/{key_orni})")
            
            key_cang = f"canguros/{self.cang.nombre}"
            self.db.create(key_cang, self.cang.to_dict())
            print(f"  -> Datos guardados en RTDB (ruta: /{self.db.base_path}/{key_cang})")
            
            key_elef = f"elefantes/{self.elef.nombre}"
            self.db.create(key_elef, self.elef.to_dict())
            print(f"  -> Datos guardados en RTDB (ruta: /{self.db.base_path}/{key_elef})")

            print("\n¡Animales guardados exitosamente en Firebase RTDB!")
        except Exception as e:
            print(f" Error general al intentar guardar en Firebase: {e}")