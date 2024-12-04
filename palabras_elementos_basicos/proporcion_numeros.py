import spacy
import wikipedia

wikipedia.set_lang("es")


def proporciones(termino):
    pagina = wikipedia.page(termino)
    nlp = spacy.blank('es')
    doc = nlp(pagina.content)
    numeros = [token.text for token in doc if token.like_num]
    prop = 100 * len(numeros) / len(doc)
    return round(prop, 2)


print(proporciones("Número áureo"))
print(proporciones("Morfología lingüística"))
print(proporciones("Azorín"))


def texto_numérico(termino):
    prop = proporciones(termino)
    if prop > 4.0:
        tipo = "numérico"
    else:
        tipo = "no numérico"
    return prop, tipo


términos = ["Platón", "Número primo", "Semántica",
            "Algoritmo de Luhn"]
for ter in términos:
    proporción, tipo_texto = texto_numérico(ter)
    print(f"{ter}. Tipo {tipo_texto} ({proporción})")
