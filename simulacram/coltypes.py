import pandas as pd
from faker import Faker
import logging
import numpy as np
from datetime import datetime

class ColTypes:
    def __init__(self):
        self.coltypes = {}

    def add_coltype(self, name, coltype, **kwargs):
        kwargs['type'] = coltype
        self.coltypes[name] = kwargs

    def get_coltypes(self):
        return self.coltypes
 
