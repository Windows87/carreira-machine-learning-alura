# **Vídeo 1 - Mais sobre Machine Learning**

## Resumo do Vídeo

O Machine Learning e a Inteligência Artificial se diferenciam pois a Inteligência Artificial busca transformar a máquina mais perto do humano, enquanto o Machine Learning busca ficar mais perto do que é possível fazer, em coisas mais específicas.

<img src="https://miro.medium.com/max/1934/1*SkpowKNy98lv-cTLhTXafw.png">

## Links e Artigos Relacionados
- <a href="https://arxiv.org/abs/0810.4752">Statistical Learning Theory: Models, Concepts, and Results</a>

# **Vídeo 2 - Breve Introdução ao Machine Learning**

## Resumo do Vídeo

Um programa aprende a partir de experiências E com respeito a alguma classe de tarefas T e medida de desempenho P, se o desempenho de tarefas em T, medido por P, melhora com experiências E.

### Como escolher uma futura jogada?

- Testar N possíveis jogadas permitidas

- Verificar a aptidão (fitness) ou custo de cada jogada

- Ter uma longa base dados com diversas jogadas que poderiam ser feitas à partir de cada jogada do oponente (Ruim)

- Poderíamos ter regras if-then-else, que jogará a partir dessas regras (Ruim)

- Poderíamos definir uma função matemática para avaliar cada jogada, assim não precisaríamos manter uma extensa base de dados ou regras
  - Cruzar esses outros dados também, afim de criar novas soluções

## Links e Artigos Relacionados
- <a href="http://profsite.um.ac.ir/~monsefi/machine-learning/pdf/Machine-Learning-Tom-Mitchell.pdf">Livro Machine Learning by Tom M. Mitchell</a>

- <a href="https://www.youtube.com/watch?v=F0Iby7KCXls">Por que a Inteligência Artificial não é um bando de IF-ELSE?</a> (Meu Link)

# **Vídeo 3 - Aprendizado Supervisionado vs Aprendizado não Supervisionado**

## Supervisionado

- Apresenta classes ou rótulos, ou seja, para aprender, ele utiliza exemplos de um conjunto de dados rotulados

- A partir dos dados, ele busca achar a classe correta **f:x -> y**, sendo os dados *x* e as classes *y*

## Não Supervisionado

- Tenta agrupar dados

- Tenta buscar dados estruturais

<img src="https://s3.amazonaws.com/cloudxlab/static/images/pl/ml/unsup.png">

# **Vídeo 14 - Redes Neurais: Aprendendo o Perceptron**

## Gráfico do Perceptron

O Perceptron cria um hiperplano para separar duas classes distintas e linearmente separáveis.

<img src="https://miro.medium.com/max/1200/1*GR7j6Z6HYYrwcWb6PGkqOQ.png">

## O que é o Perceptron

O Perceptron recebe valores valores de input, chamados de *x1*, *x2*, *x3*. Cada valor de input apresenta um peso *w1*, *w2*, *w3*. 

O valor *net* é a soma da multiplicação de todos os inputs com seus pesos + o valor de teta (que é sempre 1).

O *y* é uma função que calcula o valor *net*, essa função retorna **1** caso o valor de net >= 0.5 (ou algum outro valor).

<img src="https://miro.medium.com/max/3354/1*7pwA1DjBw6JDkwZQecUNiw.png">

## Gradiente Descendente

A ténica do Gradiente Descendente consiste em achar o mínimo de forma iterativa.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Gradient_descent.svg/350px-Gradient_descent.svg.png">