
# Simulador de Zoo Interactivo: Proyecto de Herencia y Arquitectura MVVM

Este repositorio documenta un proyecto de aplicación de consola que simula la interacción con entidades de un zoológico.

El objetivo principal del proyecto es demostrar la aplicación práctica de conceptos fundamentales de la Programación Orientada a Objetos (POO), específicamente la **Herencia**, así como la implementación de la arquitectura de software **MVVM (Modelo-Vista-VistaModelo)**.

Adicionalmente, el proyecto integra persistencia de datos en la nube mediante **Firebase Realtime Database**.

## Funcionalidad de la Aplicación

A continuación, se presenta el flujo de operación de la aplicación.

### 1\. Interfaz de Usuario Dinámica

Al iniciar, la aplicación presenta una interfaz de usuario en la consola. El menú principal se genera dinámicamente utilizando los datos actuales de los animales (ej. `PERRY`, `KIRA`, `DUMBO`).

\<img width="428" height="503" alt="Menú principal de la aplicación" src="[https://github.com/user-attachments/assets/2224da1e-36a8-4658-a2ab-86793ef93dd3](https://github.com/user-attachments/assets/2224da1e-36a8-4658-a2ab-86793ef93dd3)" /\>

### 2\. Ejecución de Acciones Específicas

El usuario puede seleccionar una acción del menú, y el sistema invocará el método correspondiente al objeto del animal. Cada entidad posee sus propios comportamientos únicos.

Respuesta del método `usar_trompa()` del Elefante:
\<img width="1163" height="100" alt="Respuesta del elefante" src="[https://github.com/user-attachments/assets/465401d8-3e72-4956-a209-6a3b66a42d9d](https://github.com/user-attachments/assets/465401d8-3e72-4956-a209-6a3b66a42d9d)" /\>

Respuesta del método `veneno_defensa()` del Ornitorrinco:
\<img width="973" height="103" alt="Respuesta de defensa del ornitorrinco" src="[https://github.com/user-attachments/assets/d7c38bed-350c-4a36-96c8-95b9e92710a3](https://github.com/user-attachments/assets/d7c38bed-350c-4a36-96c8-95b9e92710a3)" /\>

### 3\. Lógica de Negocio Basada en Estado

El comportamiento de la aplicación depende del estado interno de los objetos. Por ejemplo, si el objeto "Perry" tiene el atributo `genero="macho"`, la invocación del método "Revisar nido" (`poner_huevos()`) retornará la respuesta lógica apropiada.

\<img width="637" height="97" alt="Respuesta de ornitorrinco macho" src="[https://github.com/user-attachments/assets/babaa09c-8c96-4347-9131-10969d7e9b67](https://github.com/user-attachments/assets/babaa09c-8c96-4347-9131-10969d7e9b67)" /\>

### 4\. Actualización de Datos y Validación de Entrada

El sistema permite la modificación de datos en tiempo de ejecución. Se ha implementado lógica de validación (bucles `while` y condicionales `if`) para asegurar la integridad de los datos. La entrada "mujer" es rechazada, solicitando al usuario que ingrese un valor válido ("macho" o "hembra") antes de continuar.

### 5\. Dinamismo y Coherencia de Estado

Tras una actualización exitosa, el estado de la aplicación se refresca:

1.  El menú principal ahora refleja el nuevo nombre del objeto ("MIGUEL").
2.  La lógica de negocio se ajusta al nuevo estado. Dado que el objeto ahora es "hembra", el método "Revisar nido" produce un resultado diferente y coherente.

\<img width="496" height="147" alt="El menú y la lógica se actualizan" src="[https://github.com/user-attachments/assets/90eeab75-6517-4f87-be50-dc502869c16e](https://github.com/user-attachments/assets/90eeab75-6517-4f87-be50-dc502869c16e)" /\>

### 6\. Persistencia de Datos en Firebase

Al seleccionar la opción "Salir", el estado final de todos los objetos se serializa y se envía a Firebase Realtime Database. Esto asegura que los datos (incluyendo las modificaciones, como el cambio a "miguel") se persistan entre sesiones.

\<img width="1876" height="1008" alt="Consola de Firebase con datos" src="[https://github.com/user-attachments/assets/974ac776-ac39-415b-9b6d-878d4aff083e](https://github.com/user-attachments/assets/974ac776-ac39-415b-9b6d-878d4aff083e)" /\>

-----

## Arquitectura del Sistema

El proyecto evita una estructura monolítica y adopta un diseño modular basado en la **Separación de Responsabilidades**.

\<img width="692" height="556" alt="Estructura de archivos del proyecto" src="[https://github.com/user-attachments/assets/8c352635-b017-41e7-a6db-ef66f3cebbaa](https://github.com/user-attachments/assets/8c352635-b017-41e7-a6db-ef66f3cebbaa)" /\>

El proyecto implementa la arquitectura **MVVM (Modelo-Vista-VistaModelo)**:

### 1\. `model/` (El Modelo)

Contiene la lógica de negocio y la capa de acceso a datos. Es el "cerebro" de la aplicación.

  * **`domain.py`**: Define las clases de entidad (`Animales`, `Ornitorrinco`, `Canguro`, `Elefante`), sus atributos y sus métodos (comportamientos).
  * **`data.py`**: Contiene el servicio de acceso a datos (`FirebaseRealtimeService`). Es el único componente responsable de la comunicación con la base de datos externa.

### 2\. `UI/` (La Vista)

Responsable de la presentación al usuario. Es la "cara" de la aplicación.

  * **`interfaz.py`**: Contiene la clase `Interfaz`. Su única función es mostrar información en la consola (`print`) y recibir entradas del usuario (`input`). No contiene ninguna lógica de negocio.

### 3\. `view_model/` (El Vista-Modelo)

Actúa como el intermediario (o *pegamento*) entre la Vista y el Modelo.

  * **`view.py`**: Contiene la clase `Animales_View_model`. Cuando la `Interfaz` (Vista) notifica una acción del usuario (ej. "Opción 3 seleccionada"), el `VistaModelo` invoca los métodos apropiados del `Modelo` (ej. `orni.poner_huevos()`). Posteriormente, toma el resultado devuelto por el Modelo y lo formatea para que la Vista lo muestre.

Este patrón de diseño incrementa la modularidad, facilita las pruebas y mejora la mantenibilidad del código.

-----

## Configuración y Ejecución

### 1\. Configuración de Credenciales

Para la conexión con Firebase, se requieren dos archivos en el directorio raíz del proyecto (`herencia.ejercicio`):

1.  **Archivo de credenciales JSON:** El archivo de clave privada descargado desde la consola de Firebase (ej. `herencia-animal-firebase-adminsdk...json`).
2.  **Archivo de entorno (.env):** Un archivo que contiene las variables de entorno para la aplicación.

Contenido del archivo `.env`:

```.env
# Asegúrese de que este nombre coincida con su archivo JSON
FIREBASE_CREDENTIALS_JSON="herencia-animal-firebase-adminsdk-fbsvc-....json"

# La URL de su Realtime Database
FIREBASE_DB_URL="https://herencia-animal-default-rtdb.firebaseio.com/"
```

### 2\. Instalación de Dependencias

El proyecto requiere las bibliotecas `firebase-admin` y `python-dotenv`. Se instalan mediante `pip`:

```bash
pip install firebase-admin python-dotenv
```

### 3\. Ejecución del Módulo

**Importante:** Debido a la estructura modular del proyecto, los scripts no pueden ejecutarse directamente.

  * **Ejecución Incorrecta:** Invocar `python app/main.py` resultará en un `ModuleNotFoundError`, ya que el intérprete no podrá resolver las rutas de importación (ej. `from model.domain...`).

  * **Ejecución Correcta:** El programa debe ejecutarse como un **módulo** desde el directorio raíz (`herencia.ejercicio`) utilizando el indicador `-m`. Esto asegura que el directorio raíz se añada al `PYTHONPATH`, permitiendo que todas las importaciones relativas se resuelvan correctamente.

<!-- end list -->

```bash
python -m app.main
```
