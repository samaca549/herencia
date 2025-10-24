
# Simulador de Zoo Interactivo: Proyecto de Herencia y Arquitectura MVVM

Este repositorio documenta un proyecto de aplicación de consola que simula la interacción con entidades de un zoológico.

El objetivo principal del proyecto es demostrar la aplicación práctica de conceptos fundamentales de la Programación Orientada a Objetos (POO), específicamente la **Herencia**, así como la implementación de la arquitectura de software **MVVM (Modelo-Vista-VistaModelo)**.

Adicionalmente, el proyecto integra persistencia de datos en la nube mediante **Firebase Realtime Database**.

## Funcionalidad de la Aplicación

A continuación, se presenta el flujo de operación de la aplicación.

### 1\. Interfaz de Usuario Dinámica

Al iniciar, la aplicación presenta una interfaz de usuario en la consola. El menú principal se genera dinámicamente utilizando los datos actuales de los animales (ej. `PERRY`, `KIRA`, `DUMBO`).

<img width="549" height="447" alt="{7B9AC1C0-0F21-428B-9239-0F07F079A648}" src="https://github.com/user-attachments/assets/1affa495-2e2e-41a7-a903-fe24cef66aa2" />


### 2\. Ejecución de Acciones Específicas

El usuario puede seleccionar una acción del menú, y el sistema invocará el método correspondiente al objeto del animal. Cada entidad posee sus propios comportamientos únicos.

Respuesta del método `usar_trompa()` del Elefante:
<img width="786" height="76" alt="{E2D16092-BC67-4F51-BA14-DBBD93D390E4}" src="https://github.com/user-attachments/assets/c8456738-1d6f-4cbf-9da1-a638dbe0a887" />

Respuesta del método `veneno_defensa()` del Ornitorrinco:

<img width="954" height="88" alt="{9E63344C-0058-483B-88C8-555D8919A3C7}" src="https://github.com/user-attachments/assets/021b0b9e-1cd2-46e7-beea-34d1dba94c39" />

### 3\. Lógica de Negocio Basada en Estado

El comportamiento de la aplicación depende del estado interno de los objetos. Por ejemplo, si el objeto "Perry" tiene el atributo `genero="macho"`, la invocación del método "Revisar nido" (`poner_huevos()`) retornará la respuesta lógica apropiada.

<img width="630" height="148" alt="{A81816F8-E775-45C4-9E67-631017485A96}" src="https://github.com/user-attachments/assets/f06fff99-feda-464d-ad59-061c7fb1f89b" />


### 4\. Actualización de Datos y Validación de Entrada

El sistema permite la modificación de datos en tiempo de ejecución. Se ha implementado lógica de validación (bucles `while` y condicionales `if`) para asegurar la integridad de los datos. La entrada "mujer" es rechazada, solicitando al usuario que ingrese un valor válido ("macho" o "hembra") antes de continuar.
<img width="466" height="171" alt="{94EAAA16-E082-4A91-ABA5-7ECCEEE1D785}" src="https://github.com/user-attachments/assets/394483cf-70d9-42fc-9d1b-ace6a76bc665" />

### 5\. Dinamismo y Coherencia de Estado

Tras una actualización exitosa, el estado de la aplicación se refresca:

1.  El menú principal ahora refleja el nuevo nombre del objeto ("MIGUEL").
2.  La lógica de negocio se ajusta al nuevo estado. Dado que el objeto ahora es "hembra", el método "Revisar nido" produce un resultado diferente y coherente.
<img width="751" height="548" alt="{847BA073-2DCB-4EDE-B058-DC70E7F0F620}" src="https://github.com/user-attachments/assets/7358b9d4-35ee-4c0f-b98b-20d76f7ee0a9" />


### 6\. Persistencia de Datos en Firebase

Al seleccionar la opción "Salir", el estado final de todos los objetos se serializa y se envía a Firebase Realtime Database. Esto asegura que los datos (incluyendo las modificaciones, como el cambio a "miguel") se persistan entre sesiones.

<img width="654" height="318" alt="{9F6D81D5-9EE9-4CBA-ABC3-04D774BA73E0}" src="https://github.com/user-attachments/assets/fb1a899d-e9c5-43a2-8af9-7b81e1101347" />

<img width="1631" height="620" alt="{6FFA1F11-A75E-4980-90E9-D91264F3B8C8}" src="https://github.com/user-attachments/assets/115aef2c-ee2d-4043-91eb-84ad269dc9c6" />
<img width="665" height="247" alt="{412284E2-CB00-4954-8EDA-47C40046E881}" src="https://github.com/user-attachments/assets/336ca65c-51af-47f0-a481-e738ae48967b" />
<img width="501" height="454" alt="{3876C848-7AA7-4C72-9CD2-EBD4E42ED03A}" src="https://github.com/user-attachments/assets/78b3393c-b9da-42ce-9976-00dcea3e9890" />

-----

## Arquitectura del Sistema

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
