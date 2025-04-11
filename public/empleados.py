import pandas as pd
import json

# Asegurate de colocar la ruta correcta al archivo "empleados.xlsx".
# Usá una cadena raw para evitar conflictos con las barras invertidas.
file_path = r"C:\Users\misad\OneDrive\Escritorio\Consulta de precios multiple\empleados.xlsx"

# Leer el Excel; header=1 usa la segunda fila como encabezados
df = pd.read_excel(file_path, header=1)

# Reemplazar valores nulos por cadena vacía (opcional, para evitar problemas en el JSON)
df.fillna("", inplace=True)

# Convertir el DataFrame a una lista de diccionarios (formato JSON)
json_data = df.to_dict(orient="records")

# Guardar el resultado en un archivo JSON llamado "empleados.json"
with open("empleados.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Archivo JSON generado: empleados.json")
