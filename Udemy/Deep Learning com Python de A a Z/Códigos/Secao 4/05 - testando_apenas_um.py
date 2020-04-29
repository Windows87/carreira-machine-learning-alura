import numpy as np
import pandas as pd
import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout

data = pd.read_csv('data.csv')

troca = {
  'M': 1,
  'B': 0
}

data_x = data[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
data_y = data[["diagnosis"]]

data_y.diagnosis = data_y.diagnosis.map(troca)

model = Sequential()

model.add(Dense(units = 32, activation = 'relu', kernel_initializer = 'random_normal', input_dim = 30))
model.add(Dropout(0.25))  
model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_normal'))
model.add(Dropout(0.25))
model.add(Dense(units = 8, activation = 'relu', kernel_initializer = 'random_uniform'))
model.add(Dense(units = 1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['binary_accuracy'])

model.fit(data_x, data_y, batch_size = 10, epochs = 500)

new = np.array([[15.80, 8.34, 118, 900, 0.10, 0.26, 0.08, 0.134, 0.178, 0.20, 0.05, 1098, 0.87, 4500, 145.2, 0.005, 0.04, 0.05, 0.015, 0.03, 0.007, 23.15, 16.64, 178.5, 2018, 0.14, 0.185, 0.84, 158, 0.363]])

prevision = model.predict(new)

print(prevision)