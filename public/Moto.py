import pandas as pd

# Ruta del archivo Excel
excel_path = r"C:\Users\misad\OneDrive\Escritorio\consulta de precios app\Lista moto chao 04-25.xlsx"

# Leer el archivo Excel usando la primera fila (índice 0) como encabezados
df = pd.read_excel(excel_path, header=0)

# Eliminar columnas y filas completamente vacías (si existen)
df.dropna(axis=1, how='all', inplace=True)
df.dropna(how='all', inplace=True)

# Exportar el DataFrame a un nuevo archivo JSON
json_path = "Nuevo_Lista_de_Precios_Moto.json"
df.to_json(json_path, orient="records", force_ascii=False, indent=2)

print(f"Archivo JSON generado: {json_path}")
