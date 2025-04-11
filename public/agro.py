import pandas as pd

# Lee el archivo Excel usando la fila 11 (índice 10 en 0-index)
df = pd.read_excel(r"C:\Users\misad\OneDrive\Escritorio\Consulta de precios multiple2\Consulta de precios multiple\agro2.xlsx", header=10)

# Opcional: mostrar las primeras filas para verificar los encabezados
print(df.head())

# Convertir el DataFrame a JSON (lista de diccionarios)
json_data = df.to_json(orient="records", force_ascii=False)

# Guardar el JSON en un archivo
with open(r"C:\Users\misad\OneDrive\Escritorio\consulta de precios app\Agro3.json" \
"", "w", encoding="utf-8") as f:
    f.write(json_data)

print("JSON generado: Lista_de_Precio_AGRO.json")
