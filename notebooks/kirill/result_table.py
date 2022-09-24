#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import string
import nltk
import nltk
import re
from nltk.stem import *
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
import numpy as np


# In[8]:


def count_table_query(table_name):
    df = pd.read_csv(table_name)
    eng_stopwords=stopwords.words("english")
    eng_stopwords.extend(['…', '«', '»', '...',';',',','tbl'])
    mystem = Mystem() 
    nltk.download('stopwords')

    def remove_punctuation(text):
        return "".join([ch if ch not in string.punctuation else ' ' for ch in text])

    def remove_multiple_spaces(text):
        return re.sub(r'\s+', ' ', text, flags=re.I)

    def lemmatize_text(text):
        tokens = mystem.lemmatize(text.lower())
        tokens = [token for token in tokens if token not in eng_stopwords and token != " "]
        text = " ".join(tokens)
        return text
    def drop_words(text):
        numr=re.findall(r'\b\d+\b',text)
        return [int(item) for item in numr]
    def remove_numbers(text):
        return ''.join([i if not i.isdigit() else ' ' for i in text])
    preproccessing = lambda text: (remove_multiple_spaces(remove_numbers(remove_punctuation(text))))
    df['type'] = list(map(preproccessing, df['query']))
    preproccessing = lambda text: (drop_words(remove_multiple_spaces(remove_punctuation(text))))
    df['preproccessed'] = list(map(preproccessing, df['query']))
    x=df['preproccessed']
    x = np.concatenate(x) #список всех таблиц с запросов
    uniq=list(set(x)) #список всех уникальных таблиц
    total = df['query']
    data=list()
    for query in total.to_list():
        data.append(query.replace("tbl_", '').replace(',', ' ').split())
    name=list()
    tab=list()
    j=0
    while j<len(data):
        i=0
        while i<len(data[j]):
            if data[j][i] == 'join' or data[j][i] == 'from' or data[j][i] == 'into' or data[j][i] == 'JOIN' or data[j][i] == 'FROM' or data[j][i] == 'INTO' or data[j][i] == 'From':
                name.append(data[j][i])
            else:
                tab.append(data[j][i])
            i+=1
        j+=1
    result = pd.DataFrame(columns = ['table_name', 'from', 'join', 'into'])

    s=0
    while s<len(uniq):
        fro=0
        into=0
        join=0
        t=0
        while t<len(tab):
            if uniq[s] == int(tab[t]):
                if (name[t] == 'from') or (name[t] == 'FROM') or (name[t] == 'From'):
                    fro+=1
                if (name[t] == 'into') or (name[t] == 'INTO'):
                    into+=1
                if (name[t] == 'join') or (name[t] == 'JOIN'):
                    join+=1
            t+=1

        result = result.append(
            [
                {
                    'table_name':uniq[s], 
                    'from':fro, 
                    'join':into, 
                    'into':join
                }
            ], ignore_index=True
        )
        s+=1

        if s % 10 == 0:
            result.to_csv(f'result_'+table_name)
    return result
    


# In[9]:





# In[ ]:




