import pandas as pd
from faker import Faker
import logging
import numpy as np
from datetime import datetime

class DataSet:
    def __init__(self, length, **kwargs):
        self.data = self.create(length, **kwargs)

    def get_data(self):
        return self.data

    def num_data(self, ty, length):
        a = ty['min']
        b = ty['max']
        return pd.Series(np.random.uniform(a, b, length))

    def num_int(self, ty, length):
        a = ty['min']
        b = ty['max']
        return pd.Series(np.random.random_integers(a, b, length))

    def norm_data(self, ty, length):
        if len(ty) == 1:
            return pd.Series(np.random.standard_normal(size=length))

        mean = ty['mean']
        sd = ty['sd']
        return pd.Series(np.random.normal(mean, sd, length))

    def exp_data(self, ty, length):
        B = float(1)/float(ty['lam'])
        return pd.Series(np.random.exponential(B, length))

    def binom_data(self, ty, length):
        n = ty['n']
        p = ty['p']
        return pd.Series(np.random.binomial(n, p, length))

    def poisson_data(self, ty, length):
        lam = ty['lam']
        return pd.Series(np.random.poisson(lam, length))

    def text_data(self, ty, length):
        res = []
        f = Faker()
        for _ in range(0, length - 1):
            res.append(f.text())
        return pd.Series(res)

    def name_data(self, ty, length):
        res = []
        f = Faker()
        for _ in range(0, length - 1):
            res.append(f.name())
        return pd.Series(res)

    def cats_data(self, ty, length):
        res = []
        f = Faker()
        for _ in range(0, length - 1):
            res.append(f.name())
        return pd.Series(res)

    def date_data(self, ty, length):
      #TODO add error handling and validation for date strings passed
        res = []
        f = Faker()
        begin = datetime.strptime(ty['begin'], '%Y-%m-%d')
        end = datetime.strptime(ty['end'], '%Y-%m-%d')
        for _ in range(0, length - 1):
            res.append(f.date_time_between_dates(datetime_start=begin,
                                                 datetime_end=end))
        return pd.Series(res)

    def coords_data(self, ty, length):
        pass

    def address_data(self, ty, length):
        res = []
        f = Faker()
        for _ in range(0, length - 1):
            res.append(f.address())
        return pd.Series(res)

    def zip_data(self, ty, length):
        res = []
        f = Faker()
        for _ in range(0, length - 1):
            res.append(f.name())
        return pd.Series(res)

    def create(self, length, cols=None, types=None, coltypes=None):
        series_res = {}
        ops = {'num': self.num_data,
               'int': self.num_int,
               'norm': self.norm_data,
               'exp': self.exp_data,
               'bin': self.binom_data,
               'pois': self.poisson_data,
               'txt': self.text_data,
               'name': self.name_data,
               'addr': self.address_data,
               'zip': self.zip_data,
               'date': self.date_data}

        if cols and types and coltypes:
            logging.error('coltypes should not be defined when cols and types are defined')

        if (cols and not types) or (types and not cols):
            logging.error('cols and types must both be defined together, as lists')

        if (cols and types):
            validate_types(types)
            if len(cols) != len(types):
                logging.error('cols and types must be lists of equal length')
            for i in len(cols):
                series_res[col[i]] = ops[types[i]['type']](types[i], length)

        else:
            if not coltypes:
                logging.error('please define either cols and types or coltypes')
            for col, typ in coltypes.iteritems():
                series_res[col] = ops[typ['type']](typ, length)

        return pd.DataFrame(series_res)
