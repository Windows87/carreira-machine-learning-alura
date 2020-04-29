import pandas as pd
import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('data.csv')

troca = {
  'M': 1,
  'B': 0
}

data_x = data[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
data_y = data[["diagnosis"]]

data_y.diagnosis = data_y.diagnosis.map(troca)

def criarRede(optimizer, loss, kernel_initializer, activation, neurons):
  model = Sequential()

  model.add(Dense(units = neurons, activation = activation, kernel_initializer = kernel_initializer, input_dim = 30))
  model.add(Dropout(0.2))  
  model.add(Dense(units = neurons, activation = activation, kernel_initializer = kernel_initializer))
  model.add(Dropout(0.2))
  model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
  model.add(Dense(units = 1, activation = 'sigmoid'))

  model.compile(optimizer = optimizer, loss = loss, metrics = ['binary_accuracy'])

  return model

  classifier = KerasClassifier(build_fn = criarRede)

params = {
  'batch_size': [10, 30],
  'epochs': [50, 100],
  'optimizer': ['adam', 'sgd'],
  'loss': ['binary_crossentropy', 'hinge'],
  'kernel_initializer': ['random_uniform', 'normal'],
  'activation': ['relu', 'tanh'],
  'neurons': [16, 8]
}

grid_search = GridSearchCV(estimator = classifier, param_grid = params, scoring = 'accuracy', cv = 5)

grid_search = grid_search.fit(data_x, data_y)
best_params = grid_search.best_params_
best_precision = grid_search.best_score_