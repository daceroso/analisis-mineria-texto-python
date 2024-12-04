print("Me dijo: 'a ver si nos vemos pronto'")

a = """Mi infancia son recuerdos
de un patio de Sevilla
mi juventud, veinte años en tierras de Castilla
"""

print(a)

s = "el ser que puede ser comprendido es lenguaje (Gadamer)"
print(s.startswith("el"), s.endswith("el"))

p1 = s.find("ser")
p2 = s.find("ser", p1+1)
p3 = s.find("ser", p2+1)
pf = s.rfind("ser")
print(p1, p2, p3, pf)


# lower devuelve copia del string


s1 = "Te lo habia dicho"
s2 = "te lo habia dicho"


iguales1 = s1==s2
iguales2 = s1.lower() == s2.lower()
print(iguales1, iguales2)


r = "¡¡¡bien!!!"
print(r.lstrip("¡").rstrip("!"))


frase = "compra tomates, pepinos, calabacin, pimiento verde y ajo"
_frase = frase.replace(",", " ")
print(_frase)


cadena = "era de noche pero llovia"
l = ["era", "de", "noche", "pero", "llovia"]

print(cadena.split())
print(" ".join(l))