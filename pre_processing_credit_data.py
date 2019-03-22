#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:41:10 2019

@author: eugenio
"""

import pandas as pd # importando a biblioteca pandas

base = pd.read_csv('credit_data.csv') #carregando o arquivo de dados na variavel 'base'
base.describe() # fazendo a leitura dos dados do dataframe