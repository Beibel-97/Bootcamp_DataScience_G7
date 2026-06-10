# Paso 1: Crear un entorno virtual

Crear un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

---

# Paso 2: Activar el entorno virtual

### Windows

```bash
source venv/Scripts/activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Si la activación fue exitosa, verás el nombre del entorno virtual al inicio de la consola:

```bash
(venv) $
```

---

# Paso 3: Instalar las dependencias del proyecto

Instalar todas las librerías definidas en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```