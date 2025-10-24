
from model.domain import Animales, Ornitorrinco, Canguro, Elefante

from view_model.view import Animales_View_model

from UI.interfaz import Interfaz

from model.data import FirebaseRealtimeService  
def main():
    # --- 1. INICIALIZAR SERVICIO FIREBASE (RTDB) ---
    try:
        db_service = FirebaseRealtimeService(base_path="animales_zoo")
    except Exception as e:
        print(f" ERROR FATAL al inicializar Firebase: {e}")
        return 

    info_general = Animales(0, "variable", "multi")

    orni_macho = Ornitorrinco(5, "ovíparo", "Ornithorhynchus anatinus", "ríos", "saludable", "macho", "larvas", "alerta", "Perry")
    canguro = Canguro(6, "vivíparo", "Macropus rufus", "sabanas", "activo", "hembra", "Kira")
    elefante = Elefante(12, "vivíparo", "Loxodonta africana", "sabana", "fuerte", "macho", "Dumbo", 150, True)

    
    vm = Animales_View_model(db_service, info_general, orni_macho, canguro, elefante)
    interfaz = Interfaz(vm)
    interfaz.mostrar_menu_principal()
    vm.guardar_animales_en_firebase()

if __name__ == "__main__":
    main()