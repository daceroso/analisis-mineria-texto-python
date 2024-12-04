# ya sabemos que las listas son mutables

lista = [50, 60, 80, 90]
lista[1] = 70
print(lista)

# tuplas y string no son mutables


# para añadir usamos el metodo append, no devuelve una lista nueva sino que modifica la original
herramientas = ['tornillos', 'tuercas', 'arandelas']
herramientas.append('clavos')
print(herramientas)


caja = [['tornillos', 'tuercas', 'arandelas'], ['martillo', 'sierra']]
caja[0].append('clavos')
print(caja)
