import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import nltk
from nltk import tokenize

dados = pd.read_csv('imdb-reviews-pt-br.csv')

palavras = " ".join([texto for texto in dados.text_pt])

# Tokenização
tokenEspaco = tokenize.WhitespaceTokenizer()
token = tokenEspaco.tokenize(palavras)

frequencia = nltk.FreqDist(token)

dataframe = pd.DataFrame({ "Palavra": list(frequencia.keys()), "Frequência": list(frequencia.values()) })

print(dataframe)

# Gráfico
dataframeMaiores = dataframe.nlargest(columns = "Frequência", n = 10)

plt.figure(figsize=(12,8))
ax = sns.barplot(data = dataframeMaiores, x = "Palavra", y = "Frequência", color = 'gray')

plt.show()

# Retirando Stop Words

stopWords = nltk.corpus.stopwords.words("portuguese")
opiniaoProcessada = list()

for opiniao in dados.text_pt:
    novaOpiniao = list()
    palavrasOpiniao = tokenEspaco.tokenize(opiniao)

    for palavra in palavrasOpiniao:
        if palavra not in stopWords:
            novaOpiniao.append(palavra)
    
    opiniaoProcessada.append(' '.join(novaOpiniao))

dados['tratamento-1'] = opiniaoProcessada