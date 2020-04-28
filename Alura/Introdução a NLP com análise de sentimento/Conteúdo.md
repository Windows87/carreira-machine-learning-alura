# Aula 01

## O que deve ser feito primeiro?
Deve se conhecer as informações e ler alguns textos para compreender como é a escrita do texto.

# Aula 02

## É possível extrair dados de textos sem valor (Se é positivo ou negativo)?
Sim, utilizando algoritmos não supervisionados. Caso não queira utilizar esse tipo de aprendizagem, os textos podem serem lidos e rotulados por você mesmo ou utilizar outra base de dados já rotulados para treino e utilizar os seus dados como teste.

## O que é Processamento de Linguagem Natural (PLN)?
Tentar processar a linguagem humana para o computador.

## O que é Análise de Sentimentos?
Tentar buscar um sentimento, em textos, imagens ou outras mídias.

## Bag of Words (Sacola de Palavras)

- O filme é muito bom
- O filme é muito ruim
- O filme é muito muito bom
- O filme é **péssimo**

| O | filme | é | muito | bom | ruim |
|---|-------|---|-------|-----|------|
| 1 | 1     | 1 | 1     | 1   | 0    |
| 1 | 1     | 1 | 1     | 0   | 1    |
| 1 | 1     | 1 | **2** | 1   | 0    |
| 1 | 1     | 1 | 0     | 0   | 0    |

# Aula 03

## O que é WordCloud?
É uma imagem que é gerada utilizando as principais palavras de um texto, e cada palavra é proporcional a presença dela nesse texto.

# Aula 04

## O que é Tokenização?
É receber um texto e separar as palavras e pontuações.