import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

data = pd.read_csv('Iris.csv')

data_x = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
data_y = data[['Species']]

labelEncoder = LabelEncoder()
data_y = labelEncoder.fit_transform(data_y)
#data_y = np_utils.to_categorical(data_y)

train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size = 0.25)

def criarRede():
  model = Sequential()

  model.add(Dense(units = 4, activation = 'relu', input_dim = 4))
  model.add(Dense(units = 4, activation = 'relu'))
  model.add(Dense(units = 3, activation = 'softmax'))

  model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])

  return model

classifier = KerasClassifier(build_fn = criarRede, epochs = 100, batch_size = 10)
result = cross_val_score(estimator = classifier, X = data_x, y = data_y, cv = 10, scoring = 'accuracy')

mean = result.mean()
deviation = result.std()

print(mean)
print(deviation)