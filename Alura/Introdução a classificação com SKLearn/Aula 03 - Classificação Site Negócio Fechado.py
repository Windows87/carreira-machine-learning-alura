from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import numpy
import pandas
import seaborn
import matplotlib.pyplot as plt

dados = pandas.read_csv('https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv')

# Visualização de Dados Juntos
seaborn.scatterplot(x='expected_hours', y='price', hue='unfinished', data=dados)
plt.show()

# Visualização de Dados Separados
seaborn.relplot(x='expected_hours', y='price', hue='unfinished', col='unfinished', data=dados)
plt.show()

dados_x = dados[['expected_hours', 'price']]
dados_y = dados[['unfinished']]

treino_x, teste_x, treino_y, teste_y = train_test_split(dados_x, dados_y, test_size = 0.2, random_state = 20, stratify = dados_y)

print("Treinamento com", len(treino_x), "e Teste com", len(teste_x))

model = LinearSVC()
model.fit(treino_x, treino_y)

previsao = model.predict(teste_x)

print("Taxa de sucesso de", accuracy_score(teste_y, previsao) * 100, "%")

# Taxa de Sucesso de Previsão de Linha de Base (Chute)
previsaoLinhaDeBase = numpy.ones(432)
print("Taxa de sucesso de", accuracy_score(teste_y, previsaoLinhaDeBase) * 100, "%")