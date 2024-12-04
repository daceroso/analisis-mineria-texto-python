"""

def nombreFuncion (param1, param2, param3...):
    instruccion1
    instruccion2
    ....
    return valor
"""


def os_as(palabra):
    if palabra.endswith("os"):
        salida = palabra[:-2] + "as"
    else:
        salida = palabra
    return salida


print(os_as("poderosos"))
print(os_as("animosos"))
print(os_as("altas"))


def sufijo(palabra, s="mente"):
    salida = palabra + s
    return salida


print(sufijo("facil", "mente"))
print(sufijo("facil", "es"))
print(sufijo("dificil"))


def prefijos_sufijo(palabra, prefijo="", sufijo=""):
    salida = prefijo + palabra + sufijo
    return salida


print(prefijos_sufijo("mar", "sub", "ino"))
print(prefijos_sufijo("facil", sufijo="mente"))
print(prefijos_sufijo("diluviano", prefijo="ante"))
