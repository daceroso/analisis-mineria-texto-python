import spacy

texto = "Desde lo alto se divisa la ciudad y toda la campiña"
dividido = texto.split(" ")
print(dividido)

_texto = "Se remueve, levanta una tenue polvareda, avanza"
_dividido = _texto.split(" ")
print(_dividido)

nlp = spacy.blank('es')
s = "Se remueve, levanta una tenue polvareda, avanza"
doc = nlp(s)

l = [token.text for token in doc]
print(l)

comas = l.count(",")
print(comas)

# remove signos

frase = "@bertoldo: ¡estuvimos en el parque de atracciones!"
_doc = nlp(frase)
unidades = [token.text for token in _doc if not token.is_punct]
print(unidades)
