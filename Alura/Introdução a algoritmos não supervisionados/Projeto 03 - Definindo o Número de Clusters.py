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

# Visualização da Taxa de Inertia
def kmeans(numeroDeClusters, generos):
    model = KMeans(n_clusters = numeroDeClusters)
    model.fit(generos)
    return [numeroDeClusters, model.inertia_]

resultado = [kmeans(numeroDeClusters, generosEscalados) for numeroDeClusters in range(1, 41)]
resultado = pd.DataFrame(resultado, columns=['clusters', 'inertia'])

resultado.inertia.plot(xticks=resultado.clusters)
plt.show()