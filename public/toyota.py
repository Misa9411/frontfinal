import pandas as pd

# Leer el archivo Excel; header=1 indica que la fila 2 es la cabecera (recordando que las filas se indexan desde 0)
df = pd.read_excel("toyota a valor.xlsx", header=1)

# Convertir a JSON con formato de lista de registros, cuidando caracteres especiales y con indentación para mejor lectura
json_data = df.to_json(orient="records", force_ascii=False, indent=4)

# Escribir el JSON a un archivo (opcional)
with open("toyota.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print(json_data)
