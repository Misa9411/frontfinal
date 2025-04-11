import pandas as pd

# Nombre del archivo Excel (asegúrate de que esté en el mismo directorio o especifica la ruta completa)
excel_file = 'Lista de precios E-Commerce - 04.25 - a valor (1).xlsx'

# Leer el archivo Excel, indicando que la fila 8 (índice 7) contiene los encabezados
df = pd.read_excel(excel_file, header=7)

# Convertir el DataFrame a JSON con formato "records" (lista de diccionarios)
json_data = df.to_json(orient='records', force_ascii=False, indent=2)

# Guardar el JSON en un archivo (por ejemplo, ecommerce.json)
with open('ecommerce.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
