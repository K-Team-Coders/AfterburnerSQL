from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage    
from django.core.files.base import ContentFile
from django.conf import settings

from rest_framework.views import APIView

from .apps import MainConfig

import string
from string import punctuation
from loguru import logger
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords')
import re
import os
from nltk.stem import *
from nltk.corpus import stopwords
from pymystem3 import Mystem
from pathlib import Path

class countTableUsability(APIView):
    def post(self, request):
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

            result.to_csv(table_name+f'_result')
            return result
        
        path = 0
        file_objs = request.data.getlist('file')
        for file_obj in file_objs:
            path = os.path.join(settings.CSV_ROOT, file_obj.name)
            logger.debug(path)
            default_storage.save(path, ContentFile(file_obj.read())) 
        
        dataframe = count_table_query(path)
        logger.debug(dataframe)
        
        ready_joins = []
        ready_intos = []
        ready_froms = []

        names = dataframe['table_name'].to_list()
        froms = dataframe['from'].to_list()
        joins = dataframe['join'].to_list()
        intos = dataframe['into'].to_list()

        froms_sum = sum(froms)
        joins_sum = sum(joins)
        intos_sum = sum(intos)

        most_wanted = 0
        maximum = 0
        for index in range(len(names)):
            if (froms[index] + joins[index] + intos[index]) > maximum:
                maximum = froms[index] + joins[index] + intos[index]
                most_wanted = {
                    'count': maximum,
                    'table': names[index]
                }

            ready_joins.append({
                'x':names[index],
                'y':joins[index]
            })
            ready_froms.append({
                'x':names[index],
                'y':froms[index]
            })
            ready_intos.append({
                'x':names[index],
                'y':intos[index]
            })

        return JsonResponse({
            'from': ready_joins,
            'join': ready_joins,
            'into': ready_intos,
            'sum_into': intos_sum,
            'sum_joins': joins_sum,
            'sum_froms': froms_sum,
            'most_wanted': most_wanted
        })

class countUserActivity(APIView):
    def post(self, request):
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
            return result
        path = 0
        logger.debug(request)
        file_objs = request.data.getlist('file')
        for file_obj in file_objs:
            path = os.path.join(settings.CSV_ROOT, file_obj.name)
            logger.debug(path)
            default_storage.save(path, ContentFile(file_obj.read())) 
        
        index_list = []
        nodes = [] # [{'name': 'user'}, {'name':'user'}]
        edges = [] # [{'source':0, 'target':0, 'realation':'into', 'value': 1}]

        dataframe = count_table_id(path)

        for user in dataframe['id']:
            nodes.append({'name':user})
            
            # help list
            index_list.append(user)

            part_df = dataframe[dataframe['id'] == user]
            # FROM
            froms = part_df['from'].values[0]
            for from_ in froms:
                if from_ in index_list:
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'from',
                        'value': 1
                    })
                else:
                    index_list.append(from_)
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'from',
                        'value': 1
                    })
            # INTO
            froms = part_df['into'].values[0]
            for from_ in froms:
                if from_ in index_list:
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'into',
                        'value': 1
                    })
                else:
                    index_list.append(from_)
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'into',
                        'value': 1
                    })    
            # JOIN
            froms = part_df['join'].values[0]
            for from_ in froms:
                if from_ in index_list:
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'from',
                        'value': 1
                    })
                else:
                    index_list.append(from_)
                    edges.append({
                        'source':index_list.index(user),
                        'target':index_list.index(from_),
                        'relation': 'from',
                        'value': 1
                    })    

        return JsonResponse({
            'nodes':nodes,
            'edges': edges
            })

class predictQueryResponseTime(APIView):
    def get(self, request, query):
        logger.debug(query)
        query_list = str(query).replace(',', ' ').split()
        query_encoded_vector = []
        for item in query_list:
            part_df = MainConfig.encoding_dataframe[MainConfig.encoding_dataframe['value'] == item.lower()]
            if part_df.empty:
                return JsonResponse({"result": 'incorrect id or operators not in low registery'})
            else:
                query_encoded_vector.append(float(part_df['code'].values[0]))
        query_encoded_vector.extend([0.0] * (515 - len(query_encoded_vector))) 
        logger.debug(query_encoded_vector)       
        predicted_time = MainConfig.query_time_execution_model.predict(np.array([query_encoded_vector]))

        logger.debug(predicted_time[0][0])
        return JsonResponse({
            "result": float(predicted_time[0][0])
        })

class predictQueryResponseTimeOperatorsCount(APIView):
    def get(self, request, query):
        logger.debug(query)
        query_list = str(query).lower().replace(',', ' ').split()
        
        froms = query_list.count('from')
        joins = query_list.count('join')
        intos = query_list.count('into')
        
        predicted_time = MainConfig.operators_count_skolkovo_regressor.predict(np.array([[froms, joins, intos]]))

        logger.debug(predicted_time)
        return JsonResponse({
            "result": float(predicted_time)
        })

class predictQueryResponseTimeDesicionTree(APIView):
    def get(self, request, query):
        logger.debug(query)
        query_list = str(query).replace(',', ' ').split()
        query_encoded_vector = []
        for item in query_list:
            part_df = MainConfig.encoding_dataframe[MainConfig.encoding_dataframe['value'] == item.lower()]
            if part_df.empty:
                return JsonResponse({"result": 'incorrect id or operators not in low registery'})
            else:
                query_encoded_vector.append(float(part_df['code'].values[0]))
        query_encoded_vector.extend([0.0] * (515 - len(query_encoded_vector))) 
        logger.debug(query_encoded_vector)       
        predicted_time = MainConfig.query_time_execution_model_decision_tree.predict(np.array([query_encoded_vector]))

        logger.debug(predicted_time[0][0])
        return JsonResponse({
            "result": float(predicted_time[0][0])
        })