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


def crear_estadisticas_json_simple(dicc, campo, ruta_out):
    resultado = crear_dicc_estad(dicc, campo)
    with open(ruta_out, 'w', encoding="UTF-8") as fichero_json:
        json.dump(resultado, fichero_json)


pelis_json_estad = "ficheros/pelis_estad1.json"

crear_estadisticas_json_simple(dicc_pelis, 'año', pelis_json_estad)


def crear_estadisticas_json_estructurado(dicc, campo, campos, ruta_out):
    estad = crear_dicc_estad(dicc, campo)
    lista = []

    for (k, v) in estad.items():
        dicc = {campos[0]: k, campos[1]: v}
        lista.append(dicc)
    resultado = {"estadisticas": lista}

    with open(ruta_out, "w", encoding="UTF-8") as fichero_json:
        json.dump(resultado, fichero_json)


_pelis_json = "ficheros/pelis_estad_v1.json"
campos = ["Valor", "Apariciones"]
crear_estadisticas_json_estructurado(dicc_pelis, "año", campos, _pelis_json)
