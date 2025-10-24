Aquí tienes un README con un tono más relajado, pero explicando todo en detalle y usando tus imágenes.

-----

# 🐾 Simulador de Zoo Interactivo 🐾

¡Hola\! Este es un proyecto de consola que te permite "jugar" con los animales de un zoológico.

Lo especial de este proyecto no es solo lo que hace, sino *cómo está construido por dentro*. Es un ejemplo perfecto para aprender a organizar un programa de Python de forma limpia y profesional, usando **Herencia** (Programación Orientada a Objetos) y una arquitectura llamada **MVVM**.

Ah, y todo lo que haces se guarda en la nube usando **Firebase**.

## 📸 ¿Qué hace el programa?

Aquí tienes un vistazo de cómo funciona, paso a paso.

### 1\. El Menú de Bienvenida

Cuando inicias el programa, te recibe un menú. Fíjate que es "inteligente": te muestra los nombres reales de los animales (`PERRY`, `KIRA` y `DUMBO`).

### 2\. Dando Órdenes a los Animales

Puedes elegir una acción del menú y el animal responderá. Cada uno tiene sus propias habilidades únicas.

Aquí le pedimos al elefante Dumbo que use su trompa:

Y aquí vemos la defensa especial de Perry, el ornitorrinco:

### 3\. La Lógica Importa

El programa sabe *quién* es cada animal. Perry es "macho", así que si intentas "Revisar nido", te dirá correctamente que no puede poner huevos.

### 4\. Actualizando un Animal (con Validación)

¡Vamos a cambiar a Perry\!

1.  Elegimos la opción 10 para actualizarlo.
2.  Le queremos poner el nombre "miguel" y género "hembra".
3.  ¡Ups\! Escribimos "mujer". El programa se da cuenta, nos da un error y nos vuelve a preguntar hasta que escribimos "hembra" correctamente.

### 5\. ¡El Programa "Recuerda" el Cambio\!

¡Mira qué genial\!

1.  El menú principal ahora dice "Acciones de MIGUEL".
2.  Como "miguel" ahora es "hembra", si elegimos la opción 3 ("Revisar nido")... ¡ahora sí funciona\!

### 6\. Guardado en la Nube

Cuando terminas y eliges "Salir", el programa guarda todo en tu base de datos de Firebase. Si vas a la consola de Firebase, verás que "miguel" (hembra, furioso, etc.) está guardado perfectamente.

-----

## 🏗️ ¿Cómo está organizado por dentro? (La Arquitectura)

En lugar de poner todo en un solo archivo, separamos el código en carpetas. Esta es la clave de un proyecto limpio.

Imagina que esto es un restaurante:

### 1\. `model/` (La Cocina 👨‍🍳)

Esta carpeta es el "cerebro". No habla con el usuario, solo cocina.

  * **`domain.py`**: Son las recetas. Aquí viven las clases `Animales`, `Mamiferos`, `Ornitorrinco`... Define *qué es* un ornitorrinco y *qué puede hacer* (como `poner_huevos()` o `veneno_defensa()`).
  * **`data.py`**: Es el almacén y el repartidor. Aquí vive la clase `FirebaseRealtimeService`. Es la única que sabe cómo conectarse a Firebase para "guardar" y "pedir" ingredientes.

### 2\. `UI/` (El Cliente 👋)

Esta es la "cara" del programa, la parte que ve el usuario.

  * **`interfaz.py`**: Es el cliente en la mesa. Su único trabajo es **mostrar cosas** (`print`) y **pedir cosas** (`input`). No sabe *cómo* cocina el chef, solo pide "Quiero la opción 3".

### 3\. `view_model/` (El Mesero 🗣️)

Este es el pegamento que une todo.

  * **`view.py`**: Es el mesero (`Animales_View_model`). Es el intermediario perfecto.
    1.  Escucha al Cliente (`UI`): "¡Quiero la opción 3\!"
    2.  Va a la Cocina (`model`): "¡Chef, prepare un `poner_huevos_orni()`\!"
    3.  Toma el plato terminado (el resultado) y se lo lleva al Cliente para que lo vea.

Este método (MVVM) es increíble porque el Cocinero, el Mesero y el Cliente no necesitan saber los detalles del trabajo del otro, solo cómo comunicarse.

-----

## 🚀 ¿Cómo lo ejecuto? (Guía Rápida)

### 1\. Las Llaves (Configuración)

Necesitas dos cosas en la carpeta raíz (`herencia.ejercicio`):

1.  **Tu archivo de llave JSON:** Es el archivo que descargaste de Firebase (el que se llama `herencia-animal-firebase-adminsdk...json`).
2.  **Un archivo `.env`:** Crea un archivo nuevo con este nombre y ponle este texto:

<!-- end list -->

```.env
# Asegúrate de que este nombre sea EXACTO al de tu archivo JSON
FIREBASE_CREDENTIALS_JSON="herencia-animal-firebase-adminsdk-fbsvc-....json"

# La URL de tu Realtime Database
FIREBASE_DB_URL="https://herencia-animal-default-rtdb.firebaseio.com/"
```

### 2\. Las Herramientas (Instalación)

Abre tu terminal y escribe esto para instalar las librerías que usa el proyecto:

```bash
pip install firebase-admin python-dotenv
```

### 3\. ¡Encenderlo\! (La forma correcta de ejecutarlo)

**¡Importante\!** No puedes simplemente hacer clic en `main.py` o ejecutarlo directamente.

**❌ INCORRECTO:**
Si ejecutas `python app/main.py` te dará este error, porque no encontrará las otras carpetas (como `model`).

**✅ CORRECTO:**
Párate en la carpeta raíz (`herencia.ejercicio`) y usa el comando `-m` (que significa "módulo"). Esto le dice a Python que mire en todas las carpetas.

```bash
python -m app.main
```

¡Y listo\! Con eso, el programa se iniciará, te mostrará el menú y podrás empezar a interactuar.
