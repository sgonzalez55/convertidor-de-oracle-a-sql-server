import sqlite3

# Supongamos que tienes una variable con los datos que quieres guardar
resultado_query = "INSERT INTO tabla (columna1, columna2) VALUES ('valor1', 'valor2');"

# Nombre del archivo SQL
nombre_archivo_sql = "resultado.sql"

# Abre o crea el archivo SQL en modo escritura
with open(nombre_archivo_sql, 'w') as archivo_sql:
    # Escribe el resultado en el archivo
    archivo_sql.write(resultado_query)

print(f"Se ha guardado el resultado en el archivo {nombre_archivo_sql}")
