# crear diccionarios vacios de forma diferente


d1 = {

}

d2 = dict()

print(type(d2), type(d1))

d1['nombre'] = 'bertoldo'
d1['edad'] = 23
print(d1)

print('direccion' in d1)

d1['direccion'] = 'calle Albricias s/n'
print('direccion' in d1)

print(d1.keys(), d1.values(), d1.items())

datos_usuario = {"nombre": "Bertoldo", "edad": 23, "Calle": "calle Albricias s/n"}

for k, v in datos_usuario.items():
    print(k,v)
