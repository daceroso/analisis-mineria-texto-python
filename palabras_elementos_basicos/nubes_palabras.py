from goose3 import Goose
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# descargar noticia

g = Goose()
pag_dir = "https://elpais.com/diario/1980/12/10/cultura/345250806_850215.html"
articulo = g.extract(url=pag_dir)
texto = articulo.cleaned_text

# generar nube de palabras

nlp = spacy.blank('es')
palabras_vacias = nlp.Defaults.stop_words
w = WordCloud(stopwords=palabras_vacias)
w.generate(texto)

# mostramos el resultado

fig, ax = plt.subplots(1, 1, figsize=(20, 7), dpi=100)
plt.imshow(w)
fig.savefig("wordcloud.png")
