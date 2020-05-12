# **Seção 1: Introdução e Conteúdo do Curso**

## Conteúdo do Curso
- Algoritmo Evolucionário x Algoritmo Genético
- Componentes de um Algoritmo Genético
  - Indivíduos
  - Crossover (Reprodução)
  - Mutação
  - Seleção dos Indivíduos
- Base de Dados MySQL
- Algoritmos Genéticos com Biblioteca

## Algoritmos Evolucionários
- Modelos computacionais dos processos naturais de evolução
- Simulação da evolução das espécies
- Sobrevivência do mais apto
- Auto organização, comportamento adaptativo

## Algoritmo Genéticos
- Ramo dos algoritmos evolucionários
- Soluções cada vez melhores a partir **da evolução das gerações anteriores**
- Anda muitas vezes em conjunto com redes neurais

<img src="Photos/Secao 1/fluxograma.png">

# **Seção 2: Algoritmos Genéticos Passo a Passo**

## O que é o Indivíduo
- Indivíduos são as soluções
- Um conjunto de indivíduos formam a população
- O cromossomo (Imagem abaixo) representa uma solução (0 = Não Levar, 1 = Levar)

<img src="Photos/Secao 2/cromossomos.png">

## O que é Função de Avaliação (fitness)

- É uma medida de qualidade para avaliar se o cromossomo resolve o problema

- Se é uma solução aceitável e se pode ser utilizada para a evolução

## O que é Crossover

- Combina pedaços do cromossomos de dois indivíduos gerando filhos mais aptos

<img src="https://www.researchgate.net/profile/Javier_Ozon/publication/2263212/figure/fig3/AS:654414280925184@1533035931058/Crossover-and-mutation-operators-in-the-genetic-algorithm.png">

## O que é Mutação

- A Mutação cria diversidade, mudando aleatoriamente os genes dentro de indivíduos, é aplicado de forma menos frequente que a reprodução