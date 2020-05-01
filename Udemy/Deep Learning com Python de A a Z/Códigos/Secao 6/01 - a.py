import pandas as pd

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv('autos.csv', encoding = 'ISO-8859-1')

# Pré-Processamento: Remoção de Dados Inúteis
data = data.drop('dateCrawled', axis = 1)
data = data.drop('dateCreated', axis = 1)
data = data.drop('nrOfPictures', axis = 1)
data = data.drop('postalCode', axis = 1)
data = data.drop('lastSeen', axis = 1)

# Pré-Processamento: Remoção de Dados Desbalanceados
data = data.drop('name', axis = 1)
data = data.drop('seller', axis = 1)
data = data.drop('offerType', axis = 1)

# Pré-Processamento: Remoção de Dados Inconsistentes
data = data[data.price > 10]
data = data[data.price > 350000]

# Pré-Processamento: Valores Faltantes
values = {
  'vehicleType': 'limousine',
  'gearbox': 'manuell',
  'model': 'golf',
  'fuelType': 'benzin',
  'notRepairedDamage': 'nein'
}

data = data.fillna(value = values)

data_x = data.iloc[:, 1:13].values
data_y = data.iloc[:, 0].values

labelEncoder = LabelEncoder()

for i in [0, 1, 3, 5, 8, 9, 10]:
  data_x[:, i] = labelEncoder.fit_transform(data_x[:, i])

# Pré-Processamento: One Hot Encoder
oneHotEncoder = ColumnTransformer([('Cars', OneHotEncoder(), [0, 1, 3, 5, 8, 9, 10])], remainder='passthrough')
data_x = oneHotEncoder.fit_transform(data_x).toarray()

model = Sequential()

model.add(Dense(units = 158, activation = 'relu', input_dim = 316))
model.add(Dense(units = 158, activation = 'relu'))
model.add(Dense(units = 1, activation = 'linear'))

model.compile(loss = 'mean_absolute_error', optimizer = 'adam', metrics = ['mean_absolute_error'])

model.fit(data_x, data_y, batch_size = 300, epochs = 100)

## Verificar a Média
prevision = model.predict(data_x)
print(data_y.mean())
print(prevision.mena())