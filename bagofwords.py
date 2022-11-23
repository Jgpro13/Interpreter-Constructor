# -*- coding: utf-8 -*-
"""BagOfWords.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b9huzXNc18ACwJS8BtNkuTfm8Fn1qkmx
"""

#Aluno : Juliano Proença

# Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
# imprimir esta matriz na tela. Para tanto: 
#   a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
# onde cada item será uma das palavras da sentença. 
#   b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
# onde cada item será um lexema.
#   c) Este único corpus será usado para gerar o vocabulário. 
#   d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
# técnica bag of Words em todo o corpus.

import re 
import pandas
import requests
from bs4 import BeautifulSoup

sentencas = []
u = []
vetor = []

# sites escolhidos
links = ['https://magnimindacademy.com/blog/how-do-natural-language-processing-systems-work/',
       'https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html',
       'https://www.ibm.com/cloud/learn/natural-language-processing',
       'https://en.wikipedia.org/wiki/Natural_language_processing',
       'https://monkeylearn.com/natural-language-processing/']

# adicionando apenas as sentenças dos sites em uma lista
for pg in links:
  link = requests.get(pg).content
  soup = BeautifulSoup(link, "html.parser")
  for data in soup(['style', 'script']):
    data.decompose()
  sentenca = ' '.join(soup.stripped_strings)
  sentenca = re.sub(r"[\n\t]","", sentenca)
  split = re.split("[!?.;:,]", sentenca)
  sentencas.append(" ".join(split))

# verificando se existe ambiguidade entre as palavras dentro do vetor
def verifica_palavra(p):
  naoex = set()
  for array in p:
    for sentenca in array.split():
      naoex.add(sentenca)
  return naoex

u = verifica_palavra(sentencas)
u = list(u)
print(len(u))

# gerando matriz resultado
def gera_matriz(array_sentenca, texto):
  array = [0] * len(array_sentenca)
  for string in texto.split():
    array[array_sentenca.index(string)] += 1
  return array

for array in sentencas:
  vetor.append(gera_matriz(u, array))

dataframe = pandas.DataFrame(vetor, columns=u)
display(dataframe)