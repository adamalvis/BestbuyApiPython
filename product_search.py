from route import Route

class ProductSearch(Route):

    DEFAULTS = {
        'show': 'sku,name,longDescription',
        'pageSize': 25,
        'format': 'json',
        'apiKey': '',
    }

    def __init__(self, settings):

        self.settings = ProductSearch.DEFAULTS
        Route.__init__(self, settings)


    def search(self, params):

        params = self.format_params(params)
        endpoint = 'products({params})'.format(params=params)
        url = self.get_full_url(endpoint)

        return self.execute(url)