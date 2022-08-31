class Venue():
    __table__ = 'venues'
    columns = ['foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):

        # verify all of the keyword arguments match the columns for the table
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} is not in columns: {self.columns}')

        # add the keyword arguments to the class instance
        for k, v in kwargs.items():
            setattr(self, k, v)

