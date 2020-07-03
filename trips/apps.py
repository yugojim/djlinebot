from django.apps import AppConfig
import os
from mysite import settings
import pickle

class TripsConfig(AppConfig):
    path = os.path.join(settings.MODELS, '0GradientBoostingRegressor')
    with open(path, 'rb') as f:
        reg1 = pickle.load(f)