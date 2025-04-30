# datos_taller_3
Taller 3 ingeniería de datos con python

---

## INSTRUCCIONESS:

### pip setup:

Crear entorno virtual

linux:

```bash
python3 -m venv .venv
```
```bash
source ./src/.venv/bin/activate
```
```bash
pip install
```
```bash
pip install -r requirement.txt
```
```bash
python3 ./src/main.py
```
---

windows:

```bash
python -m venv .venv
```
```bash
./src/venv/Source/activate
```
```bash
pip install -r requirement.txt
```
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

