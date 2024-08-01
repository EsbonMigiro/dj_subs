from django.db import models
from .mongod_connector import db
# Create your models here.

person_collection = db['Person']
