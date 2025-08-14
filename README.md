# Calculadora
Calculadora generado con IA

## Ejecutar la aplicación (Streamlit)

### Requisitos
- Python 3.9 o superior

### Pasos rápidos (Windows PowerShell)
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

La app se abrirá en tu navegador en `http://localhost:8501`.

### Funcionalidades
- Operaciones básicas: suma, resta, multiplicación, división
- Operaciones científicas: potencia, raíz cuadrada, log10, factorial
- Historial de las últimas operaciones

### Estructura
- `app.py`: Aplicación Streamlit
- `requirements.txt`: Dependencias