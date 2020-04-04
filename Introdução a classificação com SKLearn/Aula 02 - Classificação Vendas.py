from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import pandas

# Obtenção dos dados CSV
dados = pandas.read_csv('https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv')

# Separação em Dados X e Dados Y
dados_x = dados[['home', 'how_it_works', 'contact']]
dados_y = dados[['bought']]

# Separação em Dados de Treino em Python Puro
treino_x = dados_x[:75]
treino_y = dados_y[:75]

# Separação em Dados de Teste em Python Puro
#teste_x = dados_x[75:]
#teste_y = dados_y[75:]

# Separação em Dados de Teste com SkLearn (Faz Separação Aleatória)
treino_x, teste_x, treino_y, teste_y = train_test_split(dados_x, dados_y, test_size = 0.25)

# Separação em Dados de Teste com SkLearn (Com Seed)
SEED = 20
treino_x, teste_x, treino_y, teste_y = train_test_split(dados_x, dados_y, random_state = SEED, test_size = 0.25)

# Separação em Dados de Teste com SkLearn (Com Proporção)
SEED = 20
treino_x, teste_x, treino_y, teste_y = train_test_split(dados_x, dados_y, random_state = SEED, stratify = dados_y, test_size = 0.25)

print("Treinamento com", len(treino_x), "e Teste com", len(teste_x))

model = LinearSVC()
model.fit(treino_x, treino_y)

previsao = model.predict(teste_x)

print("Taxa de sucesso de", accuracy_score(teste_y, previsao) * 100, "%")