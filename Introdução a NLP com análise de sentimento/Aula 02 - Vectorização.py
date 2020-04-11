import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

textos = ['É um filme ótimo', 'É um filme ruim']

vetorizador = CountVectorizer()
bagOfWords = vetorizador.fit_transform(textos)
dicionario = vetorizador.get_feature_names()

bagOfWordsSparseDataFrame = pd.DataFrame.sparse.from_spmatrix(bagOfWords, columns=dicionario)

print(bagOfWordsSparseDataFrame)