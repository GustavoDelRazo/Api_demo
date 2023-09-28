from fastapi import FastAPI
import csv
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    # Inicializar una lista para almacenar los datos de los contactos
    contactos = []

    try:
        # Abrir el archivo CSV y leer los datos
        with open("contactos.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contactos.append(row)
    except FileNotFoundError:
        return {"error": "El archivo de contactos no fue encontrado"}

    # Codificar los datos de contacto en formato JSON
    contactos_json = json.dumps(contactos)

    # Crear la respuesta con los datos codificados en JSON
    response = {"contactos": contactos_json}
    return response
