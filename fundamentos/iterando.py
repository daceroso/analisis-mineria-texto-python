for h in ['tornillos', 'tuercas', 'arandelas']:
    print(h)


#usando range

for i in range(11):
    if i % 2 == 0: # si el resto al dividir entre 2 es 0 es par
        print(i)


pares = []

for i in range(101):
    if i % 2 == 0:
        pares.append(i)
print(pares)


for i in range(len(pares)):
    if pares[i] % 3 == 0:
        print(pares[i])

print("Bucle alternativo")

for elem in pares:
    if elem % 3 == 0:
        print(elem)


# posicion y valor con enumerate


for pos, elem in enumerate(pares):
    print(f"En la posicion {pos} encontramos el elemento {elem}")