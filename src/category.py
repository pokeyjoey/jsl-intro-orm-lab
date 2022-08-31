class Category:
    __table__ = 'categories'
    columns = ['name']

    def __init__(self, **kwargs):
        # verify keyword arguments are in the table
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')

        # set the class instance attributes
        for k, v in kwargs.items():
            setattr(self, k, v)

