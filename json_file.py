import json


def load_json(ruta):
    with open(ruta, 'r', encoding="UTF-8") as fichero_json:
        dicc = json.load(fichero_json)
    return dicc


pelis_json = "ficheros/pelis.json"
dicc_pelis = load_json(pelis_json)

print(dicc_pelis)


def crear_dicc_estad(dicc, campo):
    peliculas = dicc["peliculas"]
    resultado = {}

    for peli in peliculas:
        valor = peli[campo]
        if valor in resultado:
            resultado[valor] = resultado[valor] + 1
        else:
            resultado[valor] = 1
    return resultado


estadisticas = crear_dicc_estad(dicc_pelis, 'año')

print(estadisticas)
