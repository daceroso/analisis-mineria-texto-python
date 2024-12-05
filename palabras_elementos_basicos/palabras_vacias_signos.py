import spacy

nlp = spacy.blank('es')

frase = "Platón murió a los 80 años de edad, dedicándose en sus últimos años de vida a impartir enseñanzas en la Academia"
# incluye varias veces estos terminos

nlp.Defaults.stop_words.add("platón")
nlp.Defaults.stop_words.add("academia")
# cuando no debe removerse

nlp.Defaults.stop_words.remove("últimos")

# palabras vacias predeterminadas

palabras_vacias = ["el", "la", "los", "las", "a", "en", "sus", "de"]
doc = nlp(frase)

l = [token.text for token in doc if not token.text.lower() in palabras_vacias and not token.is_punct]

print(l)
