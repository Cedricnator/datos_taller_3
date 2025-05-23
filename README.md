# TALLER 3 INGENIERIA DE DATOS - [ICC732-1]
Taller 3 ingeniería de datos con python
Entrenamiento de un Modelo de Clasificación

- Integrantes:
-- Eduardo Arevalo: e.arevalo01@ufromail.cl
-- Cedric Kirmayr: c.kirmayr01@ufromail.cl
---

## **INSTRUCCIONESS**:

### Clonar repositorio:
1. Clonar con HTTPS:
```bash
git clone https://github.com/Cedricnator/datos_taller_3.git
```
o Clonar con SSH:
```bash
clone git@github.com:<Usuario>/datos_taller_3.git
```
2. Entrar en el repositorio:
```bash
cd datos_taller_3
```

### pip setup:

#### Linux y MacOS:
1. Entorno virtual
```bash
python3 -m venv .venv
```
2. Acticar entorno virtual
```bash
source ./src/.venv/bin/activate
```
3. Instalar dependencias
```bash
pip install -r requirement.txt
```

4. Ejecutar main.py(OPCIONAL)
```bash
python3 ./src/main.py
```

---

#### windows:

1. Crear entorno virtual
```bash
python -m venv .venv
```

2. Activar entorno virtual
```bash
./src/venv/Source/activate
```

3. Instalar dependencias
```bash
pip install -r requirement.txt
```

4. Ejecutar main.py(OPCIONAL)
```bash
python ./src/main.py
```


### [uv](https://github.com/astral-sh/uv):

if uv is not installed:
```bash
pip install -r requirement.txt
```
```bash
uv sync
```
```bash
uv run ./src/main.py
```

