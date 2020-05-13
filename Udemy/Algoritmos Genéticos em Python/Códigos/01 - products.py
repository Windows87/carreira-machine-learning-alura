from random import random

import matplotlib.pyplot as plt

# Classe Produto
class Product:
  def __init__(self, name, space, value):
    self.name = name
    self.space = space
    self.value = value

    # Classe Indivíduo
class Individual:
  def __init__(self, names, spaces, values, spaceLimit, chromosome = [], generation = 0):
    self.names = names
    self.spaces = spaces
    self.values = values
    self.spaceLimit = spaceLimit
    self.generation = generation
    self.chromosome = chromosome
    self.usedSpace = 0
    self.rating = 0

    isChromosomeEmpty = not len(chromosome)

    if(isChromosomeEmpty):
      self.generateFirstGeneration()

    self.fitness()

  def generateFirstGeneration(self):
    for i in range(len(self.spaces)):
      if random() < 0.5:
        self.chromosome.append('0')
      else:
        self.chromosome.append('1')

  def setChromosome(self, chromosome):
    self.chromosome = chromosome
  
  def crossover(self, anotherIndividual):
    crossoverPoint = round(random() * len(self.chromosome))

    childOneChromosome = anotherIndividual.chromosome[0:crossoverPoint] + self.chromosome[crossoverPoint::]
    childTwoChromosome = self.chromosome[0:crossoverPoint] + anotherIndividual.chromosome[crossoverPoint::]

    children = [Individual(self.names, self.spaces, self.values, self.spaceLimit, childOneChromosome, self.generation + 1),
                Individual(self.names, self.spaces, self.values, self.spaceLimit, childTwoChromosome, self.generation + 1)]
    
    return children


  def mutate(self, mutateProbability):
    for i in range(len(self.chromosome)):
      if random() < mutateProbability:
        if self.chromosome[i] == '1':
          self.chromosome[i] = '0'
        else:
          self.chromosome[i] = '1' 

  def fitness(self):
    rating = 0
    spaceSum = 0

    for i in range(len(self.chromosome)):
      if self.chromosome[i] == '1':
        rating += self.values[i]
        spaceSum += self.spaces[i]

    if spaceSum > self.spaceLimit:
      rating = 1

    self.rating = rating
    self.usedSpace = spaceSum

  def showIndividualData(self):
    print('----- PRODUTOS ESCOLHIDOS -----')
    
    for i in range(len(self.chromosome)):
      if(self.chromosome[i] == '1'):
        print(self.names[i] + ' - R$' + str(self.values[i]) + ' - ' + str(self.spaces[i]))
    
    print('---------- RESULTADOS ----------')

    print('Espaço Utilizado: ' + str(self.usedSpace))
    print('Nota: ' + str(self.rating))

    # Classe Algoritmo Genético
class GeneticAlgorithm:
  def __init__(self, populationLength, mutationRate):
    self.populationLength = populationLength
    self.mutationRate = mutationRate
    
    self.population = []
    self.generation = 0
    self.bestSolution = 0

  def initializePopulation(self, names, spaces, values, spaceLimit):
    for i in range(self.populationLength):
      individual = Individual(names, spaces, values, spaceLimit, [])
      self.population.append(individual)
    self.sortPopulation()
    self.bestSolution = self.population[0]

  def sortPopulation(self):
    self.population = sorted(self.population, key = lambda population: population.rating, reverse = True)

  def getRatingSum(self):
    sum = 0

    for individual in self.population:
      sum += individual.rating
    
    return sum

  def showBestSolutionNumber(self):
    return self.bestSolution.rating

  def selectFather(self):
    father = -1
    randomValue = random() * self.getRatingSum()

    sum = 0
    i = 0

    while i < len(self.population) and sum < randomValue:
      sum += self.population[i].rating
      father += 1
      i += 1

    return father

  def createNewPopulation(self):
    newPopulation = []

    for i in range(0, self.populationLength, 2):
      fatherOne = self.selectFather()
      fatherTwo = self.selectFather()

      children = self.population[fatherOne].crossover(self.population[fatherTwo])

      children[0].mutate(self.mutationRate)
      children[1].mutate(self.mutationRate)

      newPopulation.append(children[0])
      newPopulation.append(children[1])
    
    self.population = newPopulation + self.population
    self.sortPopulation()
    self.population = self.population[0:self.populationLength]
    self.bestSolution = self.population[0]

# Cria a Lista de Produtos
products = []

productNames = ['Geladeira Dako', 'iPhone 6', 'TV 55p', 'TV 50p', 'TV 42p', 'Notebook Dell', 'Ventilador Panasonic', 'Microondas Electrolux', 'Microondas LG', 'Microondas Panasonic', 'Geladeira Brastemp', 'Geladeira Consul', 'Notebook Lenovo', 'Notebook Asus']
productSpaces = [0.751, 0.0000899, 0.400, 0.290, 0.200, 0.00350, 0.496, 0.0424, 0.0544, 0.0319, 0.635, 0.870, 0.498, 0.527]
productValues = [999.90, 2911.12, 4346.99, 3999.90, 2999.00, 2499.90, 199.90, 308.66, 429.90, 299.29, 849.00, 1199.89, 1999.90, 3999.00]

for i in range(len(productNames)):
  products.append(Product(productNames[i], productSpaces[i], productValues[i]))

# Limite de Espaço de 3m^3
spaceLimit = 3

def getBestOfBests():
  bestOfBests = None
  listOfSuperBests = []

  for i in range(10):
    print('---------------- SuperGeração ' + str(i) + ' ----------------')

    best = None
    listOfBests = []

    geneticAlgorithm = GeneticAlgorithm(100, 0.05)
    geneticAlgorithm.initializePopulation(productNames, productSpaces, productValues, spaceLimit)

    for k in range(200):
      geneticAlgorithm.createNewPopulation()
      print('Geração ' + str(k + 1) + ': Best -> ' + str(geneticAlgorithm.showBestSolutionNumber()))

      listOfBests.append(geneticAlgorithm.showBestSolutionNumber())

      if(not best):
        best = geneticAlgorithm.bestSolution

      if(geneticAlgorithm.showBestSolutionNumber() > best.rating):
        best = geneticAlgorithm.bestSolution
      
    
    plt.plot(listOfBests)
    plt.title('Gráfico da SuperGeração ' + str(i))
    plt.show()

    listOfSuperBests.append(best.rating)

    if(not bestOfBests):
      bestOfBests = best

    if(bestOfBests.rating < best.rating):
      bestOfBests = best

  plt.plot(listOfSuperBests)
  plt.title('Gráfico Final das SuperGerações')
  plt.show()

  bestOfBests.showIndividualData()

getBestOfBests()