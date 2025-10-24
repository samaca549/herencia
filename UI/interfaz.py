from view_model.view import Animales_View_model
# Ya no necesitamos 'import time'

class Interfaz:
    def __init__(self, metodos: Animales_View_model):
        self.metodos = metodos

    def pedir_datos_ornitorrinco(self):
        """
        Validación de datos con 'while' e 'if'.
        """
        print(f"\n🦦 ACTUALIZAR DATOS DE {self.metodos.orni.nombre.upper()}")
        
        nombre = ""
        while not nombre:
            nombre = input("Digite el nuevo nombre del ornitorrinco: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío. Intente de nuevo.")
        
        genero = ""
        while genero not in ["macho", "hembra"]:
            genero = input("Digite el género (macho/hembra): ").strip().lower()
            if genero not in ["macho", "hembra"]:
                print("Error: Por favor, escriba 'macho' o 'hembra'.")

        alimentos = input(f"Digite los alimentos que caza {nombre}: ").strip()
        estado = input(f"Digite el estado de ánimo de {nombre}: ").strip()

        # Actualizamos los datos
        self.metodos.orni.nombre = nombre
        self.metodos.orni.genero = genero
        self.metodos.orni.alimentos = alimentos
        self.metodos.orni.estado = estado
        
        print(f"\n✅ ¡Datos del ornitorrinco '{nombre}' actualizados correctamente!")


    def mostrar_menu_principal(self):
        """
        Bucle principal del programa. Interactivo pero más simple y rápido.
        """
        print("\n¡Bienvenido al Simulador Interactivo de Zoo!")
        print("============================================")

        while True:
            
            # --- MENÚ DINÁMICO ---
            # Lee los nombres actuales de los animales
            nombre_orni = self.metodos.orni.nombre
            nombre_cang = self.metodos.cang.nombre
            nombre_elef = self.metodos.elef.nombre

            print(f"\n---  Acciones de {nombre_orni.upper()} (Ornitorrinco) ---")
            print("1. Alimentar")
            print("2. Defender")
            print("3. Revisar nido")
            
            print(f"\n---  Acciones de {nombre_cang.upper()} (Canguro) ---")
            print("4. Hacer saltar")
            print("5. Revisar marsupio")
            print("6. Ver comportamiento social")
            
            print(f"\n--- Acciones de {nombre_elef.upper()} (Elefante) ---")
            print("7. Usar la trompa")
            print("8. Mostrar colmillos")
            print("9. Recordar rutas")
            
            print("------------------------------------------")
            print(f"10. Actualizar datos de {nombre_orni}")
            print("11. Salir (y guardar en Firebase)")
            
            opcion = input("\nSeleccione una opción (1-11): ").strip()

            # --- Lógica 'if/elif/else' (más directa) ---
            if opcion == "1":
                print(f"\n Acción: {self.metodos.alimentar_orni()}")
            
            elif opcion == "2":
                print(f"\n Acción: {self.metodos.defender_orni()}")
            
            elif opcion == "3":
                print(f"\n Acción: {self.metodos.poner_huevos_orni()}")
            
            elif opcion == "4":
                print(f"\n Acción: {self.metodos.saltar_cang()}")
            
            elif opcion == "5":
                print(f"\n Acción: {self.metodos.revisar_marsupio_cang()}")
            
            elif opcion == "6":
                print(f"\n Acción: {self.metodos.ver_social_cang()}")
            
            elif opcion == "7":
                print(f"\n Acción: {self.metodos.usar_trompa_elef()}")
            
            elif opcion == "8":
                print(f"\n Acción: {self.metodos.mostrar_colmillos_elef()}")
            
            elif opcion == "9":
                print(f"\n Acción: {self.metodos.recordar_rutas_elef()}")
            
            elif opcion == "10":
                self.pedir_datos_ornitorrinco()
            
            elif opcion == "11":
                print("\nSaliendo del programa y guardando datos en Firebase...")
                break  # Rompe el bucle 'while True'
            
            else:
                print(f"\n❌ Error: '{opcion}' no es una opción válida. Intente de nuevo.")