# **Seção 1: Introdução**

## Exemplos de Usos
- **Redes adversárias generativas**: Gerar imagens de números
- **Autoencoder**: Decodificação
- **Boltzmann Machines**: Sistema de Recomendação
- **Mapa autoorganizáveis**: Detecção de fraudes
- **Redes neurais recorrentes**: Previsão do Preço de Ações
- **Redes neurais convolucionais**: Visão Computacional
- **Redes neurais artificial**: Detectar câncer

## Canal do Youtube do Autor
<a href="https://www.youtube.com/channel/UCaGrIWpwjWXT6OIQh9W4Riw/videos">Clique aqui</a>

## Outros Exemplos
- Detecção de objetos
- Detecção de faces
- Text to Speech
- Tradução
- Diagnóstico de Câncer de Pele
- Redução de Custos
- Doenças em Plantas
- Qualificar Legumes
- Carros Autônomos
- Aplicação em Jogos (ex: Poker)
- Geração Automática de Músicas
- Criação de Roteiros
- Geração de Imagens Automáticas

## Gráfico de Redes Neurais
<img src="https://miro.medium.com/max/4000/1*cuTSPlTq0a_327iTPJyD-Q.png">

*Nota do Autor*: "Já vi trabalhos de reconhecimento de câncer em imagem que utilizam mais de 100 camadas ocultas"

### Se as redes neurais datam de 1950, por que somente agora as redes neurais tem desempenho superior a outros algoritmos?
Pois não havia um desempenho computacional bom e não havia dados suficientes.

# **Seção 2: Redes Neurais Artificiais**

## Curso mais Avançado (c/ Teoria) sobre Redes Neurais
<a href="https://www.udemy.com/course/redes-neurais-artificiais-em-python/">Clique Aqui</a>. Foi implementado apenas utilizando a linguagem Python sem bibliotecas.

## Conceitos
- **Neurônio Artificial**: um neurônio artificial possui entradas com pesos que irá passar por uma Função Soma e outra função de ativação (no caso Step Function abaixo).

<img src="./Photos/Secao 2/neuronio-artificial.png">

- **Perceptron**: Técnica usada para problemas linearmente separáveis (ex. Operador "and").

- **Não Linearmente Separável**: Não é possível separar por uma linha linear, problemas não linearmente separáveis devem utilizar mais camadas.

<img src="https://juliocprocha.files.wordpress.com/2017/07/figura_1.jpg?w=646">

- **Rede Neural Multicamada**: Rede neural que utiliza mais de uma camada (ex. Operador "XOR"). 

- **Função Sigmoid**: Função bastante utilizada em redes neurais multicamadas.

<img src="./Photos/Secao 2/sigmoid.png">

- **Cálculo do Erro Simples**: Pode ser calculado com "respostaCorreita - respostaCalculada", quanto menor, melhor.

<img src="./Photos/Secao 2/calculoErro.png">

- **Cálculo do Gradiente**: Tentar encontrar a combinação de pesos que o erro é o menor possível, tentar descobrir como ajustar melhor esse peso (diminuir ou aumentar o peso).
  - Função Ativação (Sigmoid)
  - Derivada da Função (Derivada do Sigmoid)
  - Delta Saída (Erro * Derivada)
  - Delta Escondido (Derivada * peso * DeltaSaída)
  - Gradiente
  - Atualização dos Pesos

<img src="./Photos/Secao 2/gradiente.png">

<img src="./Photos/Secao 2/gradienteDeltaEscondido.png">

<img src="./Photos/Secao 2/ajustePeso.png">

<img src="./Photos/Secao 2/ajustePeso2.png">

<img src="./Photos/Secao 2/ajustePeso3.png">

<img src="./Photos/Secao 2/ajustePeso4.png">

- **Bias**: Neurônio invisível que é configurável pelas próprias bibliotecas, que vai ser constante e não varia com as entradas.

- **Mean Square Error**: Penaliza os erros mais que o cálculo de erro simples.

<img src="./Photos/Secao 2/mse.png">

- **Gradient Descent Stochastic (SGD)**: Ajuda a prevenir mínimos locais e é mais rápido.

- **Parâmetros**:
  - **Learning Rate**: Indica o ritmo que os pesos são atualizados, o que pode ser estático ou adaptado. O método mais utilizado é o *Adam*.

  - **Batch Size**: Tamanho de exemplos de treinamentos utilizados em uma iteração.

  - **Epochs**: Vai rodar várias iterações tentando modificar os pesos.

## Função de Ativação

- **Step (Função Degrau)**: É utilizada em problemas linearmente separáveis, que retorna um valor 0 ou 1. Caso seja menor que 1, será retornado 0. Implementação em ```01 - step.py```.

<img src="./Photos/Secao 2/step.png">

- **Sigmoid (função sigmoide)**: É utilizado em probabilidade, que retorna um valor entre 0 e 1. Implementação em ```02 - sigmoid.py```.

<img src="./Photos/Secao 2/sigmoid.png">

- **Hyperbolic tanget (função tangente hiperbólica)**: Também é utilizado em classificação, retorna um valor entre -1 e 1. Implementação em ```03 - hyperbolic.py```.

<img src="./Photos/Secao 2/hyperbolic.png">

- **ReLU (rectified linear units)**: Retornar zero ou valores maiores. É muito utilizada em redes neurais convolucionais e redes neurais profundas. Implementação em ```04 - relu.py```.

<img src="./Photos/Secao 2/relu.png">

- **Linear**: Utilizada em regressão. Implementação em ```05 - linear.py```.

<img src="./Photos/Secao 2/linear.png">

- **Softmax**: Retorna probabilidades para cada uma das classes, utilizado em quando há mais de duas classes. Implementação em ```06 - softmax.py```.

<img src="./Photos/Secao 2/softmax.png">

## Outras Fontes Utilizadas
<a href="https://stanford.edu/~shervine/l/pt/teaching/cs-229/dicas-aprendizado-profundo">Dicas de aprendizado profudo - Stanford EDU</a>

<a href="http://deeplearningbook.com.br/o-efeito-do-batch-size-no-treinamento-de-redes-neurais-artificiais/">O Efeito do Batch Size no Treinamento de Redes Neurais Artificiais - Deep Learning Book</a>

# **Seção 4: Classificação binária - base breast cancer**

## Link para download do Data Set
<a href="https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29">Clique aqui</a>

## Como saber quantos Neurônios utilizar
Utilize a equação *(entradas + saídas) / 2*. No exemplo da Seção 4, são 30 entradas e 1 saída, então a equação seria de *(30 + 1) / 2* com resultado 15.5, mas arredondado para 16.

## K-fold Cross Validation
A divisão de testes e treinamento pode ter um problema que alguns registros de teste poderiam contribuir muito mais se estivessem na base de dados de treinamento (que generalizariam mais).

Com isso, entra a abordagem do K-Fold Cross Validation (Validação Cruzada), que busca encontrar os melhores dados de treinamento. Essa técnica é muito utilizada em pesquisas científicas.

<img src="./Photos/Secao 2/kfold-cross-validation.png">

Quase todos os trabalhos utilizam o **K = 10**, pois não há muito sentido utilizar valores muito altos. Disponível em ```02 - cross_validation.py```

## Overfitting e Underfitting

<img src="./Photos/Secao 4/underfitting-e-overfitting.png">

- **Overfitting**: Utilizar muitos recursos para um problema simples (o que pode acabar viciando com os dados, as vezes não conseguindo classificar corretamente).
  - Resultados bons na base de treinamento
  - Resultados ruins na base de teste
  - Muito específico
  - Memorização

<img src="./Photos/Secao 4/overfitting.png">

- **Underfitting**: Utilizar poucos recursos para um problema complexo.
  - Resultados ruins na base de treinamento

<img src="./Photos/Secao 4/underfitting.png">

- **Bom modelo**

<img src="./Photos/Secao 4/bom-modelo.png">

## Dropout
O dropout zera neurônios aleatoriamente. O valor recomendado é de 20% a 30%. Disponível em ```01 - dropout.py```

## Tuning (ajuste) dos parâmetros
Disponível em ```04 - tuning.py```, o resultado pode demorar horas para ser calculado, pois busca os melhores testes para a rede neural.

# **Seção 5: Base Íris**

## Diferenças entre Binário e Diferentes Itens
  - Número de unidades de saídas
  - Função de Ativação Softmax
  - Função de loss
  - Função de metrics

# **Seção 6: Base de Carros Usados**

## Link do Download do Dataset
<a href="https://www.kaggle.com/orgesleka/used-cars-database">Clique Aqui</a>

## Pré-Processamentos
- **Dados Inúteis**: Remova os dados inúteis, ou seja, que não vão ajudar a classificar os dados.

- **Desbalanceamento**: Veja se existe um desbalanceamento entre atributos (ex. um atributo "Tipo de Venda" apresenta 10.000 valores como "Venda Direta" e "3" como "Leilão", logo, esse atributo pode ser retirado).

- **Inconsistentes**: Veja se há dados que não são consistentes (ex. preço muito baixo ou muito alto).

- **Valores Faltantes**: Caso existam dados faltantes (NaN), faça um pré-processamento deles. No curso esses dados faltantes foram trocados por valores mais utilizados.

- **One Hot Encoder**: Utilize isso para aqueles valores que não possuem um peso caso sejam diferentes (ex. tipo de carro, tipo de linguagem, etc.), pois um tipo de carro classificado como "0" não será melhor que um tipo de carro classificado como "1".

## Diferenças de um Problema de Regressão
- Utilizar a função de ativação linear na última camada, pois queremos um número e não uma probabilidade.

# **Seção 9: Redes Neurais Convolucionais**

## No que é utilizado?
Utilizado em Visão Computacional: carros autônomos, análise de imagens.

## Exemplo utilizando apenas cores
Esses valores numéricos mostram as cores (Laranja camisa, Azul calção, etc.). Porém isso pode não ser muito efetivo em alguns outros trabalhos.

<img src="./Photos/Secao 9/homer.png">

## Redes neurais densas x Convolucionais
- Não usa todas as entradas (pixels)

- Usa uma rede neural tradicional, mas no começo transforma os dados na camada de entrada (extrai apenas as informações relevantes).

## Etapas
- **Etapa 1: Operador de convolução:** Processo de adicionar cada elemento da imagem para seus vizinhos, ponderado por um <a href="https://en.wikipedia.org/wiki/Kernel_(image_processing)"> kernel</a>.

<img src="./Photos/Secao 9/convolucao.png">

- **Etapa 2: Pooling:** Seleciona as características mais relevantes (reduz overfitting e ruídos desnecessários). De uma matriz, pega o valor maior pra compor a nova matriz.

<img src="./Photos/Secao 9/pooling.png">

- **Etapa 3: Flattening:** Transformação de um vetor 2D para um array 1D.

<img src="./Photos/Secao 9/flattening.png">

- **Resumo:** Convolução -> ReLu -> Pooling -> Flattening -> Rede Neural Densa

<img src="./Photos/Secao 9/resumo.png">