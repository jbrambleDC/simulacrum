class ColTypes:
    def __init__(self):
        self.coltypes = {}

    def add_coltype(self, name, coltype, **kwargs):
        kwargs['type'] = coltype
        self.coltypes[name] = kwargs

    def get_coltypes(self):
        return self.coltypes
 
