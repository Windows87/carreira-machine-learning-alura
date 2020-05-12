from random import random

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

    childOne = anotherIndividual.chromosome[0:crossoverPoint * self.chromosome[crossoverPoint::]]
    childTwo = self.chromosome[0:crossOverPoint * anotherIndividual.chromosome[crossoverPoint::]]

    children = [Individual(self.names, self.spaces, self.values, self.spaceLimit, childOne),
                Individual(self.names, self.spaces, self.values, self.spaceLimit, childTwo)]


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
    self.fitness()

    print('----- PRODUTOS ESCOLHIDOS -----')
    
    for i in range(len(self.chromosome)):
      if(self.chromosome[i] == '1'):
        print(self.names[i] + ' - R$' + str(self.values[i]) + ' - ' + str(self.spaces[i]))
    
    print('---------- RESULTADOS ----------')

    print('Espaço Utilizado: ' + str(self.usedSpace))
    print('Nota: ' + str(self.rating))

# Classe Algoritmo Genético
class GeneticAlgorithm:
  def __init__(self, populationLength):
    self.populationLength = populationLength
    self.population = []
    self.generation = 0
    self.bestSolution = 0

  def initializePopulation(self, names, spaces, values, spaceLimit):
    for i in range(self.populationLength):
      individual = Individual(names, spaces, values, spaceLimit, [])
      self.population.append(individual)
    self.bestSolution = self.population[0]

  def sortPopulation(self):
    self.population = sorted(self.population, key = lambda population: population.rating, reverse = True)

  def getRatingSum(self):
    sum = 0

    for individual in self.population:
      sum += individual.rating
    
    return sum

  def showBestSolution(self):
    self.bestSolution.showIndividualData()

# Cria a Lista de Produtos
products = []

productNames = ['Geladeira Dako', 'iPhone 6', 'TV 55p', 'TV 50p', 'TV 42p', 'Notebook Dell', 'Ventilador Panasonic', 'Microondas Electrolux', 'Microondas LG', 'Microondas Panasonic', 'Geladeira Brastemp', 'Geladeira Consul', 'Notebook Lenovo', 'Notebook Asus']
productSpaces = [0.751, 0.0000899, 0.400, 0.290, 0.200, 0.00350, 0.496, 0.0424, 0.0544, 0.0319, 0.635, 0.870, 0.498, 0.527]
productValues = [999.90, 2911.12, 4346.99, 3999.90, 2999.00, 2499.90, 199.90, 308.66, 429.90, 299.29, 849.00, 1199.89, 1999.90, 3999.00]

for i in range(len(productNames)):
  products.append(Product(productNames[i], productSpaces[i], productValues[i]))

# Limite de Espaço de 3m^3
spaceLimit = 3

geneticAlgorithm = GeneticAlgorithm(20)
geneticAlgorithm.initializePopulation(productNames, productSpaces, productValues, spaceLimit)

geneticAlgorithm.showBestSolution()
print(geneticAlgorithm.getRatingSum())