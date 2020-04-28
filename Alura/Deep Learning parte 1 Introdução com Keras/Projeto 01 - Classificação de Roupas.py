import tensorflow
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

## Pegar dados do Dataset
dataset = keras.datasets.fashion_mnist
((treino_x, treino_y),(teste_x, teste_y)) = dataset.load_data()

# Visualização das Imagens
classificacao = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

'''
for imagem in range(10):
  plt.subplot(2, 5, imagem+1)
  plt.imshow(treino_x[imagem])
  plt.title(classificacao[treino_y[imagem]])
'''

## plt.show()

# Visualização da Barra de Cores

plt.imshow(treino_x[0])
plt.colorbar()

## plt.show()

# Normalização (Conversão de cores para float)
treino_x = treino_x/255.0

# Criação do Modelo
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),
  keras.layers.Dense(256, activation=tensorflow.nn.relu),
  keras.layers.Dropout(0.2), 
  keras.layers.Dense(10, activation=tensorflow.nn.softmax)
])

# Compilando
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinando
historico = model.fit(treino_x, treino_y, epochs=10, validation_split=0.2)

# Plotando o gráfico da acurácia

plt.plot(historico.history['accuracy'])
plt.plot(historico.history['val_accuracy'])

plt.title('Acurácia por épocas')
plt.xlabel('épocas')
plt.ylabel('acurácia')
plt.legend(['treino', 'validação'])

## plt.show()

# Plotando o gráfico de perda

plt.plot(historico.history['loss'])
plt.plot(historico.history['val_loss'])

plt.title('Perda por épocas')
plt.xlabel('épocas')
plt.ylabel('perda')
plt.legend(['treino', 'validação'])

## plt.show()

# Testando

##testes = model.predict(teste_x)
##print(f'Resultado: {np.argmax(testes[0])}')

perda, acuracia = model.evaluate(teste_x, teste_y)
print(f'Perda: {perda * 100}%')
print(f'Acurácia: {acuracia * 100}%')