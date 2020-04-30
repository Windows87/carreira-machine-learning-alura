import pandas as pd
import keras

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

data = pd.read_csv('data.csv')

troca = {
  'M': 1,
  'B': 0
}

data_x = data[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
data_y = data[["diagnosis"]]

data_y.diagnosis = data_y.diagnosis.map(troca)

def criarRede():
  model = Sequential()

  model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform', input_dim = 30))
  model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
  model.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
  model.add(Dense(units = 1, activation = 'sigmoid'))

  optimizer = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)

  model.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['binary_accuracy'])

  return model

classifier = KerasClassifier(build_fn = criarRede, epochs = 100, batch_size = 10)
result = cross_val_score(estimator = classifier, X = data_x, y = data_y, cv = 10, scoring = 'accuracy')

mean = result.mean()
deviation = result.std()

print(mean)