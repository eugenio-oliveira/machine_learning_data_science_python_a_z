#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:41:10 2019

@author: eugenio
"""

import pandas as pd # importando a biblioteca pandas

base = pd.read_csv('credit_data.csv') # carregando o arquivo de dados na variavel 'base'
base.describe() # fazendo a leitura dos dados do dataframe
base.loc[ base['age'] < 0 ] # buscando os registros onde a idade for menor que zero
# base.drop('age',1,inplace=True) #f orma para apagar a coluna selecionada inteira
# base.drop(base[base.age < 0].index, inplace=True) # apaga apenas os registros errados
base.mean() # obtendo a média dos valores na base de dados
base['age'].mean() # obtendo a média das idades na base de dados
base['age'][base.age > 0].mean() # obtendo a média das idades que forem maior que zero na base de dados
base.loc[base.age < 0, 'age'] = 40.92 # ajustando as idades com valores incorretos, setando o valor da média de idades

pd.isnull(base['age'])