import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix

data = pd.read_csv('Iris.csv')

data_x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
data_y = data[['Species']]

labelEncoder = LabelEncoder()
data_y = labelEncoder.fit_transform(data_y)
data_y = np_utils.to_categorical(data_y)

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size = 0.25)

model = Sequential()

model.add(Dense(units = 4, activation = 'relu', input_dim = 4))
model.add(Dense(units = 4, activation = 'relu'))
model.add(Dense(units = 3, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])

model.fit(train_x, train_y, batch_size = 10, epochs = 1000)

# Resultado 
result = model.evaluate(test_x, test_y)

## Geração de Matriz de Confusão
prevision = model.predict(test_x)
prevision = (prevision > 0.5)

matriz_y = [np.argmax(t) for t in test_y]
prevision2 = [np.argmax(t) for t in prevision]

matriz = confusion_matrix(prevision2, matriz_y)

print(result)
print(matriz)