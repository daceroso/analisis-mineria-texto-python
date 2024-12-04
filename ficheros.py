def cargar_fichero(ruta):
    with open(ruta, 'r', encoding="UTF-8") as fichero:
        texto = fichero.read()
    return texto


mi_ruta = "ficheros/rima.txt"
mi_texto = cargar_fichero(mi_ruta)
print(mi_texto)


def cargar_lineas(ruta):
    with open(ruta, 'r', encoding="UTF-8") as fichero:
        texto = fichero.readlines()
    return texto


mi_ruta = "ficheros/rima.txt"
mis_lineas = cargar_fichero(mi_ruta)
print(mis_lineas)


def agregar_texto(ruta, texto):
    with open(ruta, 'a', encoding="UTF-8") as fichero:
        fichero.write(texto)


agregar_texto(mi_ruta, "Gustavo Adolfo Becquer")
print(mis_lineas)


def agregar_num_linea(ruta_in, ruta_out):
    lineas = cargar_lineas(ruta_in)
    num = 1
    nuevo_texto = ""
    for linea in lineas:
        nueva_linea = str(num) + " " + linea
        nuevo_texto = nuevo_texto + nueva_linea
        num = num + 1
    with open(ruta_out, 'w', encoding="UTF-8") as fichero_out:
        fichero_out.write(nuevo_texto)


ruta_out = "ficheros/rima_num_lineas.txt"
agregar_num_linea(mi_ruta, ruta_out)
