from .dataset import DataSet

def create(length, **kwargs):
    x = DataSet(length, **kwargs)
    return x.data
