import pandas as pd
import keras

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv('data.csv')

troca = {
  'M': 1,
  'B': 0
}

data_x = data[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
data_y = data[["diagnosis"]]

data_y.diagnosis = data_y.diagnosis.map(troca)

model = Sequential()

model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform', input_dim = 30))
model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
model.add(Dense(units = 1, activation = 'sigmoid'))

optimizer = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)

model.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['binary_accuracy'])
model.fit(train_x, train_y, batch_size=10, epochs = 100)

previsoes = model.predict(test_x)
previsoes = (previsoes > 0.5)

precision = accuracy_score(test_y, previsoes)
matriz = confusion_matrix(test_y, previsoes)

print(precision)