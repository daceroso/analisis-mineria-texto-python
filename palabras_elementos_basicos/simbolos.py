import spacy
import wikipedia

wikipedia.set_lang("es")

termino = "Número áureo"
pagina = wikipedia.page(termino)

nlp = spacy.blank('es')
doc = nlp(pagina.content)
numeros = [token.text for token in doc if token.like_num]
print(numeros)


proporcion_numeros = 100 *len(numeros) / len(doc)
print(proporcion_numeros)