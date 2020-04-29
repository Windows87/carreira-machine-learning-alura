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

model.add(Dense(units = 8, activation = 'relu', kernel_initializer = 'normal', input_dim = 30))
model.add(Dropout(0.2))  
model.add(Dense(units = 8, activation = 'relu', kernel_initializer = 'normal'))
model.add(Dropout(0.2))
model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
model.add(Dense(units = 1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['binary_accuracy'])

model.fit(data_x, data_y, batch_size = 10, epochs = 100)

model_json = model.to_json()

with open('model_breast.json', 'w') as json_file:
  json_file.write(model_json)

model.save_weights('model_breast.h5')