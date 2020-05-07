import pandas as pd
from keras.layers import Dense, Dropout, Activation, Input
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from keras.models import Model

data = pd.read_csv('original.csv')

# Apagar colunas irrelevantes
data = data.drop('Name', axis = 1)
data = data.drop('Other_Sales', axis = 1)
data = data.drop('Global_Sales', axis = 1)
data = data.drop('Developer', axis = 1)

# Apagar registros com Valores NaN
data = data.dropna(axis = 0)

# Apagar Valores não Consistentes
data = data.loc[data['NA_Sales'] > 1]
data = data.loc[data['EU_Sales'] > 1]

data_x = data.iloc[:, [0, 1, 2, 3, 7, 8, 9, 10, 11]].values
                   
data_y_NA = data.iloc[:, 4].values
data_y_EU = data.iloc[:, 5].values
data_y_JP = data.iloc[:, 6].values

labelEncoder = LabelEncoder()

for i in [0, 2, 3, 8]:
  data_x[:, i] = labelEncoder.fit_transform(data_x[:, i])

# Pré-Processamento: One Hot Encoder
oneHotEncoder = ColumnTransformer([('VideoGames', OneHotEncoder(), [0, 2, 3, 8])], remainder='passthrough')
data_x = oneHotEncoder.fit_transform(data_x).toarray()

inputLayer = Input(shape = (61,))

denseLayerOne = Dense(units=32, activation = 'sigmoid')(inputLayer)
denseLayerTwo = Dense(units=32, activation = 'sigmoid')(denseLayerOne)

exitLayerOne = Dense(units=1, activation='linear')(denseLayerTwo)
exitLayerTwo = Dense(units=1, activation='linear')(denseLayerTwo)
exitLayerThree = Dense(units=1, activation='linear')(denseLayerTwo)

model = Model(inputs = inputLayer, outputs = [exitLayerOne, exitLayerTwo, exitLayerThree])

model.compile(optimizer = 'adam', loss = 'mse')

model.fit(data_x, [data_y_NA, data_y_EU, data_y_JP], epochs = 5000, batch_size = 100)