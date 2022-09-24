from django.apps import AppConfig
# import tensorflow as tf
# from tensorflow import keras
from django.conf import settings
from loguru import logger
import pandas as pd
import pickle as pkl
import os

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    operators_count_skolkovo_regressor = 0
    with open(os.path.join(settings.BASE_DIR.parent, 'models/operator_count_skolkovo_regressor.pkl'), 'rb') as f:
        operators_count_skolkovo_regressor = pkl.load(f)

    # query_time_execution_model = tf.keras.models.load_model(os.path.join(settings.BASE_DIR.parent, 'models/full_query_skolkovo_model.h5'))
    logger.success('Query Time Execution model locked and loaded!')

    encoding_dataframe = pd.read_csv(os.path.join(settings.BASE_DIR.parent, 'data/encoding.csv'))
    encoding_dataframe = encoding_dataframe.drop('Unnamed: 0', axis=1)