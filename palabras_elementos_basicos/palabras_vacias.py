import spacy

nlp = spacy.blank('es')
stopwords  = nlp.Defaults.stop_words

print(len(stopwords))
print(stopwords)
