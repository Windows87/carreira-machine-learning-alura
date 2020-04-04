import pandas
import seaborn
import numpy
import matplotlib.pyplot as plt
import graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from IPython.display import Image

dados = pandas.read_csv('https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv')

troca = {
  'yes': 1,
  'no': 0
}

# Troca de Dados
dados.sold = dados.sold.map(troca)
dados['age'] = 2020 - dados.model_year
dados['km_per_year'] = dados.mileage_per_year * 1.60934

# Exclusão de Colunas
dados = dados.drop(columns = ['Unnamed: 0', 'mileage_per_year', 'model_year'])

dados_x = dados[['km_per_year', 'age', 'price']]
dados_y = dados[['sold']]

# Visualização de Gráficos
##seaborn.scatterplot(y='price', x='km_per_year', hue='sold', data=dados)
##plt.show()

#3seaborn.scatterplot(y='price', x='age', hue='sold', data=dados)
##plt.show()

# Previsão Linear
SEED = 5

numpy.random.seed(SEED)

raw_treino_x, raw_teste_x, raw_treino_y, raw_teste_y = train_test_split(dados_x, dados_y, test_size = 0.25, stratify = dados_y)

print('Treino com', len(raw_treino_x),'itens e Teste com', len(raw_teste_x))

scaler = StandardScaler()
scaler.fit(raw_treino_x)
treino_x = scaler.transform(raw_treino_x)
teste_x = scaler.transform(raw_teste_x)

modelo = LinearSVC()
modelo.fit(treino_x, raw_treino_y.values.ravel())

previsao = modelo.predict(teste_x)

print('Taxa de Acerto:', accuracy_score(raw_teste_y, previsao) * 100)

# Baseline Stratify
dummy = DummyClassifier()
dummy.fit(treino_x, raw_treino_y)

print('Taxa de Acerto Baseline:', dummy.score(teste_x, raw_teste_y) * 100)

# Decision Tree Classifier
modelTree = DecisionTreeClassifier(max_depth=4)
modelTree.fit(raw_treino_x, raw_treino_y)
previsaoTree = modelTree.predict(raw_teste_x)

print('Taxa de Acerto Decision Tree:', accuracy_score(raw_teste_y, previsaoTree) * 100)

features = dados_x.columns
dotData = export_graphviz(modelTree, filled = True, rounded = True, feature_names = features, class_names=['No', 'Yes'])
grafico = graphviz.Source(dotData)

grafico.render(filename='g7.dot')