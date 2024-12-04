pares = [i for i in range(100)  if i % 2 == 0]
print(pares)


# [expr(x) for x in secuencia if cond(x)]

palabras = ["Habia", "una", "vez" , "una", "princesa", "que", "estaba", "triste"]

a = [letra for letra in palabras if letra.endswith("a")]
print(a)

long_a = [len(letra) for letra in palabras if letra.endswith("a")]
print(long_a)

# con listas intensionales podemos extraer caracteres

letras = [letra for letra in "abracadabra"]
print(letras)