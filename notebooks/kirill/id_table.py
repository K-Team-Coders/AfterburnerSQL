#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


def count_table_id(table_name):
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
    preproccessing = lambda text: (drop_words(remove_multiple_spaces(remove_punctuation(text))))
    df['preproccessed'] = list(map(preproccessing, df['query']))
    total = df['query']
    data=list()
    i=0
    for query in total.to_list():
        data.append(query.replace("tbl_", '').replace(',', ' ').split())
    uniq=list(set(df['loguser']))
    log=list(df['loguser'])
    name=list()
    tab=list()
    user=list()
    j=0
    while j<len(data):
        i=0
        while i<len(data[j]):
            if data[j][i] == 'join' or data[j][i] == 'from' or data[j][i] == 'into' or data[j][i] == 'JOIN' or data[j][i] == 'FROM' or data[j][i] == 'INTO' or data[j][i] == 'From':
                name.append(data[j][i])
            else:
                tab.append(data[j][i])
            if i%2 == 1:
                user.append(log[j])
            i+=1
        j+=1
    result = pd.DataFrame(columns = ['id', 'from', 'join', 'into'])

    s=0
    while s<len(uniq):
        fro=list()
        into=list()
        join=list()
        t=0
        while t<len(tab):
            if uniq[s] == user[t]:
                if (name[t] == 'from') or (name[t] == 'FROM') or (name[t] == 'From'):
                    fro.append(tab[t])
                if (name[t] == 'into') or (name[t] == 'INTO'):
                    into.append(tab[t])
                if (name[t] == 'join') or (name[t] == 'JOIN'):
                    join.append(tab[t])
            t+=1

        result = result.append(
            [
                {
                    'id':uniq[s], 
                    'from':fro, 
                    'join':into, 
                    'into':join
                }
            ], ignore_index=True
        )
        s+=1

        if s % 10 == 0:
            result.to_csv(f'id_result_'+table_name)
    return result


# In[4]:





# In[ ]:




