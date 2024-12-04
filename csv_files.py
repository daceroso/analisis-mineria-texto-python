import csv


def cargar_listas(ruta, delim, agr):
    with open(ruta, encoding="latin1") as ficheroCSV:
        lector = csv.reader(ficheroCSV, delimiter=delim, quotechar=agr)
        lista = [fila for fila in lector]
    return lista


CSV_punto_coma = "ficheros/pelis_punto_coma.csv"
contenido = cargar_listas(CSV_punto_coma, ";", '"')
print(contenido)

CSV_comillas = "ficheros/pelis_comillas.csv"
contenido_comillas = cargar_listas(CSV_comillas, ",", '"')
print(contenido_comillas)


def estadistica_lista(info, index_col, ruta, delim, agr):
    dicc = {}

    for fila in info[1:]:
        valor = fila[index_col]
        if valor in dicc:
            dicc[valor] = dicc[valor] + 1
        else:
            dicc[valor] = 1

    lista = [list(par) for par in dicc.items()]  # (clave, valor)
    lista = [["Valor", "Apariciones"]] + lista  # [clave, valor]

    with open(ruta, "w", encoding="UTF-8") as fichero_csv:
        escritor = csv.writer(fichero_csv, delimiter=delim, quotechar=agr, quoting=csv.QUOTE_MINIMAL)

        for fila in lista:
            escritor.writerow(fila)


CSV_estad_punto_coma = "ficheros/pelis_punto_coma_est.csv"
estadistica_lista(contenido, 2, CSV_estad_punto_coma, ";", '"')


def cargar_dicc(ruta, delim, arg):
    with open(ruta, encoding="latin1") as fichero_csv:
        lector = csv.DictReader(fichero_csv, delimiter=delim, quotechar=arg)
        lista = [element for element in lector]
    return lista


contenido_dicc = cargar_dicc(CSV_punto_coma, ";", '"')
print(contenido_dicc)


def estadistica_dicc(info, campo, ruta, delim, arg, cab):
    acumulador = {}

    for dicc in info:
        valor = dicc[campo]
        if valor in acumulador:
            acumulador[valor] = acumulador[valor] + 1
        else:
            acumulador[valor] = 1

    with open(ruta, "w", encoding="UTF-8") as fichero_csv:
        escritor = csv.DictWriter(fichero_csv, delimiter=delim, quotechar=arg, fieldnames=cab)
        escritor.writeheader()

        for (k, v) in acumulador.items():
            dicc_actual = {cab[0]: k, cab[1]: v}
            escritor.writerow(dicc_actual)



cabecera = ["Valor", "Apariciones"]
CSV_estad_comillas = "ficheros/pelis_comillas_est.csv"
estadistica_dicc(contenido_dicc, "Año", CSV_estad_comillas,",", '"', cabecera)
