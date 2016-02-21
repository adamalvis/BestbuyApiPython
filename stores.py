from route import Route

class Stores(Route):

    DEFAULTS = {
        'format': 'json',
        'apiKey': '',
        'show': 'storeId,address,address2,city,distance,region',
    }

    def __init__(self, settings):

        self.settings = Stores.DEFAULTS
        Route.__init__(self, settings)


    def search(self, params):

        params = self.format_params(params)
        endpoint = 'stores({params})'.format(params=params)
        url = self.get_full_url(endpoint)

        return self.execute(url)