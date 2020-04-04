from sklearn.svm import LinearSVC 
from sklearn.metrics import accuracy_score

# Features
# [Pelo Longo, Perna Curta, Late]

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# 0 => Cachorro
# 1 => Porco
treino_y = [1, 1, 1, 0, 0, 0]

# Inicialização do Modelo
model = LinearSVC()

# Aprendizado Supervisionado
model.fit(treino_x, treino_y)

# Testa um Animal Misterioso
animalMisterioso = [1, 1, 1]

# Função de Prever (Ele necessita de um array de arrays)
previsao = model.predict([animalMisterioso])
print(previsao)

# Testa Varios Animais Misteriosos
misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]
teste_x = [misterio1, misterio2, misterio3]

previsao = model.predict(teste_x)
print(previsao)

# Cálculo da Taxa de Acerto
teste_y = [0, 1, 1]

# Retorna um array com True para igual e False para Diferente
print(previsao == teste_y)

# Faz a soma dos Corretos (True) e Porcentagem de Acerto com Python Puro
corretos = (previsao == teste_y).sum()
total = len(teste_x)
taxaDeAcerto = corretos/total
print("Taxa de Acerto: ", taxaDeAcerto * 100, "%")

# Porcentagem de Acerto com SkLearn
print(accuracy_score(teste_y, previsao) * 100)