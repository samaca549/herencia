Aquí tienes el `README.md` actualizado con un tono más directo y profesional, e incluyendo las imágenes que proporcionaste.

Simplemente copia y pega todo el texto de abajo en un archivo llamado `README.md` en la carpeta raíz de tu proyecto. Asegúrate de que los archivos de imagen estén en la misma carpeta o ajusta la ruta si los mueves a una subcarpeta.

-----

# Simulador de Zoo Interactivo: Proyecto de Herencia y MVVM

Este es un proyecto de aplicación de consola que simula la interacción con varios animales de un zoo.

El propósito principal es demostrar la aplicación de la **Programación Orientada a Objetos (POO)**, específicamente la **Herencia**, y la implementación de una arquitectura de software desacoplada conocida como **MVVM (Modelo-Vista-VistaModelo)**.

La aplicación se conecta a una base de datos en la nube (Firebase Realtime Database) para persistir los datos de los animales.

-----

## Características Principales

  * **Menú Interactivo en Consola:** Una interfaz de usuario que permite al usuario seleccionar acciones específicas para cada animal.
  * **Diseño Orientado a Objetos:** La lógica de los animales está modelada usando clases y herencia (`Animales` -\> `Mamiferos` -\> `Ornitorrinco`, `Canguro`, `Elefante`).
  * **Arquitectura MVVM:** El código está organizado y separado por responsabilidades (`Model`, `View`, `ViewModel`).
  * **Validación de Entradas:** La interfaz de usuario incluye lógica de validación (usando `while` e `if`) para prevenir datos incorrectos o vacíos.
  * **Persistencia de Datos:** La aplicación se conecta y guarda el estado de los animales en Firebase Realtime Database al salir.

-----

## Aplicación en Acción

A continuación, se muestra el flujo de ejecución del programa.

### 1\. Menú Principal Dinámico

El programa presenta un menú que se actualiza dinámicamente con los nombres actuales de los animales (`PERRY`, `KIRA`, `DUMBO`).

### 2\. Ejecución de Acciones

El usuario puede seleccionar una acción y el programa responde ejecutando el método correspondiente de la clase del animal.

| Acción del Elefante | Acción del Ornitorrinco (Defensa) | Acción del Ornitorrinco (Nido) |
| :---: | :---: | :---: |
|  |  |  |

### 3\. Actualización de Datos con Validación

El programa valida activamente la entrada del usuario. En este ejemplo, se rechaza el género "mujer" y se solicita una entrada válida ("macho" o "hembra") antes de continuar.

### 4\. Lógica de Programa Dinámica

Después de actualizar el ornitorrinco "Perry" a "miguel" y cambiar su género a "hembra", la lógica interna del programa se adapta.

1.  El menú principal ahora muestra el nuevo nombre ("miguel").
2.  Al seleccionar "Revisar nido", el resultado es diferente, ya que "miguel" es hembra y ahora sí puede poner huevos.

### 5\. Persistencia en Base de Datos

Al seleccionar "Salir", el estado final de los animales (incluyendo los datos actualizados de "miguel") se guarda en Firebase Realtime Database.

| Vista de la Base de Datos en Firebase | Detalle de los Datos Guardados |
| :---: | :---: |
|  |  |

-----

## Estructura del Proyecto

El proyecto está organizado en carpetas, separando las responsabilidades de la aplicación.

### 1\. La Lógica: Herencia (Clases de Datos)

  * **Clase Base (`model/domain.py` -\> `Animales`):** Define atributos comunes a todos los animales (edad, especie).
  * **Clase Intermedia (`model/domain.py` -\> `Mamiferos`):** Hereda de `Animales` y añade atributos específicos de mamíferos (hábitat).
  * **Clases Derivadas (`model/domain.py` -\> `Ornitorrinco`, `Canguro`):** Heredan de `Mamiferos` y definen sus comportamientos únicos (métodos `veneno_defensa()`, `saltar()`, `to_dict()`).

### 2\. La Arquitectura: MVVM

Este patrón divide el proyecto en tres componentes principales:

  * **`model/` (El Modelo):**

      * `domain.py`: Contiene las clases de datos (`Animales`, `Ornitorrinco`...). Define la estructura de los datos y sus reglas de negocio (los métodos de cada animal).
      * `data.py`: Contiene el servicio `FirebaseRealtimeService`. Es el único componente responsable de comunicarse con la base de datos (guardar, leer, etc.).

  * **`UI/` (La Vista):**

      * `interfaz.py`: Contiene la clase `Interfaz`. Su única responsabilidad es interactuar con el usuario. Muestra información (`print`) y recibe comandos (`input`). No contiene lógica de negocio.

  * **`view_model/` (El Vista-Modelo):**

      * `view.py`: Contiene la clase `Animales_View_model`. Actúa como el intermediario entre la Vista y el Modelo. Recibe las peticiones de la `Interfaz` ("El usuario presionó 1"), llama a los métodos adecuados del `Modelo` (`orni.detectar_alimento()`), y entrega el resultado de vuelta a la `Interfaz` para que lo muestre.

-----

## Configuración y Ejecución

Siga estos pasos para ejecutar el proyecto localmente.

### 1\. Configurar Firebase y el Archivo `.env`

La aplicación requiere credenciales de servicio de Firebase para conectarse a la base de datos.

1.  Descargue su archivo JSON de credenciales de servicio desde la consola de Firebase.
2.  Coloque este archivo JSON en la carpeta raíz del proyecto (`herencia.ejercicio`).
3.  Cree un archivo llamado `.env` en la misma carpeta raíz.
4.  Añada el siguiente contenido al archivo `.env`, asegurándose de que el nombre del archivo JSON y la URL de la base de datos sean correctos:

<!-- end list -->

```.env
# Reemplace esto con el nombre real de su archivo JSON
FIREBASE_CREDENTIALS_JSON="herencia-animal-firebase-adminsdk-....json"

# Reemplace esto con la URL de su Realtime Database
FIREBASE_DB_URL="https://herencia-animal-default-rtdb.firebaseio.com/"
```

### 2\. Instalar Dependencias

Este proyecto requiere las librerías `firebase-admin` (para Firebase) y `python-dotenv` (para leer el archivo `.env`).

```bash
pip install firebase-admin python-dotenv
```

### 3\. Ejecutar el Programa

**Importante:** Debido a la estructura de carpetas, el script no puede ejecutarse directamente.

  * **Ejecución Incorrecta:** Si intenta ejecutar `python app/main.py`, fallará con un error `ModuleNotFoundError`, ya que Python no podrá localizar la carpeta `model`.
  * **Ejecución Correcta:** Debe ejecutar el proyecto como un **módulo** desde la carpeta raíz (`herencia.ejercicio`) usando el flag `-m`.

<!-- end list -->

```bash
python -m app.main
```
