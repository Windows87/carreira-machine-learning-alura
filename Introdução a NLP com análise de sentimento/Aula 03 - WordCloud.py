import pandas as pd 
import matplotlib.pyplot as plt

from wordcloud import WordCloud

dados = pd.read_csv('imdb-reviews-pt-br.csv')

def nuvemPalavras(dadosTexto):
    palavras = " ".join([texto for texto in dadosTexto.text_pt])
    nuvem = WordCloud(width=800, height=500, collocations = False).generate(palavras)

    plt.figure()
    plt.imshow(nuvem)
    plt.show()

# Comum
#nuvemPalavras(dados)

# Positivo
nuvemPalavras(dados.query("sentiment == 'pos'"))

# Negativo
#nuvemPalavras(dados.query("sentiment == 'neg'"))