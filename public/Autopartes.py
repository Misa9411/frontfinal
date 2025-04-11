import pandas as pd
import json

# Ruta del archivo Excel
file_path = r"C:\Users\misad\Downloads\Autopartes.xlsx"

# Leé el Excel; header=7 indica que la fila 8 (índice 7) es la fila de encabezados
df = pd.read_excel(file_path, header=7)

# Opcional: reemplazar valores NaN por cadena vacía para evitar errores en el JSON
df.fillna("", inplace=True)

# Convertir el DataFrame a una lista de diccionarios en formato JSON
json_data = df.to_dict(orient="records")

# Guardar el resultado en un archivo JSON (por ejemplo, "autopartes_fixed.json")
with open("autopartes_fixed.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Archivo JSON generado: autopartes_fixed.json")
