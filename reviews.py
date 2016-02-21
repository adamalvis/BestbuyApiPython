from route import Route

class Reviews(Route):

    DEFAULTS = {
        'format': 'json',
        'apiKey': '',
        'show': 'id,sku,comment'
    }

    def __init__(self, settings):
        self.settings = Reviews.DEFAULTS
        Route.__init__(self, settings)


    def search(self, params):

        params = self.format_params(params)
        endpoint = 'reviews({params})'.format(params=params)
        url = self.get_full_url(endpoint)

        return self.execute(url)