import pandas as pd

# Leer el Excel, indicando que la fila 8 (índice 7) contiene los headers
df = pd.read_excel("retail.xlsx", header=7)

# Convertir el DataFrame a JSON en formato de lista de registros
json_data = df.to_json(orient="records", force_ascii=False, indent=4)

# Guardar el JSON resultante en un archivo
with open("retail.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print("Archivo JSON generado correctamente.")

