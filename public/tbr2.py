import pandas as pd

# Lee el archivo Excel, indicando que la fila 8 (índice 7) contiene los encabezados
df = pd.read_excel("tbr2.xlsx", header=7)

# Convierte el DataFrame a formato JSON (lista de registros) con indentación para mayor legibilidad
json_data = df.to_json(orient="records", force_ascii=False, indent=4)

# Guarda el JSON en un archivo (por ejemplo, tbr.json)
with open("tbr.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print("Archivo JSON generado correctamente: tbr.json")