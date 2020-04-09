import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

dados = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/machine-learning-algoritmos-nao-supervisionados/master/movies.csv')

# Conversão de "Comedy|Romance" para por exemplo Comedy = 1 | Romance = 1 | Animation = 0 | Musical = 0, etc.
generos = dados.genres.str.get_dummies()

# Concatena os Dataframes
dados = pd.concat([dados, generos], axis=1)

# Escalar gêneros
scaler = StandardScaler()
generosEscalados = scaler.fit_transform(generos)

# Divisão em Grupos (Clusterização)
model = KMeans(n_clusters=20)

model.fit(generosEscalados)

print(f'Grupos {model.labels_}')

# Visualização de Gráficos
grupos = pd.DataFrame(model.cluster_centers_, columns=generos.columns)
grupos.transpose().plot.bar(subplots=True, figsize=(18, 18), sharex=False)
#plt.show()

# Visualização em 2D
tsne = TSNE()
visualizacao = tsne.fit_transform(generosEscalados)

seaborn.set(rc={'figure.figsize': (13, 13)})

seaborn.scatterplot(x=visualizacao[:, 0], y=visualizacao[:, 1], hue=model.labels_, palette=seaborn.color_palette('Set1', 3))