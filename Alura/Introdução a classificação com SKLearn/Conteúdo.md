# Aula 01 - Introdução à Classificação

## Como descobrir se um animal é um Cachorro ou um Porco?
Por meio de Características (ou Features). Com mais características e mais testes envolvendo diversos porcos e cachorros, a chance de acerto da máquina aumenta.

## Como é Representado essas Características?
Como 0 (não) e 1 (sim). Por exemplo:

- Pelo Longo
- Perna Curta
- Late

Para um porco comum, seria "sim, sim, não", o que gera um vetor [1, 1, 0]. Seguindo a mesma lógica, geraria [1, 1, 1] para um tipo de cachorro, [0, 1, 1] para outro tipo de cachorro ou até [0, 0, 0] para um determinado tipo de cachorro específico.

Com isso, se nota que quanto maio3r número de Features, maior o número de fidelidade para estimar um acerto, já que como o cérebro humano, a máquina também tem uma taxa de erro.

## Padronização de Nomes

- `train_x` -> Vetor com as Features de Teste -> [[0, 1, 1], [1, 1, 0]]
- `train_y` -> Vetor com as Classes de Teste -> [0, 1]

## Ordem Correta de Treino do Algoritmo

1. Definir o Modelo do Treino
2. Definir os Vetores de Treino
3. Treinar os Dados com esses Vetores de Treino

# Aula 02 - Testes Replicáveis, Estratificação e Lendo Dados da Internet

## É importante manter uma proporcionalidade
Caso uma máquina apenas tenha aprendido que uma loja não vende durante os treinos, caso nos testes haja caso de vendas, a máquina irá entender que a loja não vende mesmo assim.

# Aula 03 - Um Projeto de Baixa Dimensionalidade e o Baseline

## O que é baseline?
A Baseline, ou Linha de Base é um parâmetro, que no caso na aula foi apenas um chute. O algoritmo deve 

# Aula 05 - Dummy classifiers e árvore de decisão

## O que são samples?
Samples são casos que foram treinados