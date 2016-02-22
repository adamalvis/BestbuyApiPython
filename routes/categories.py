from route import Route

class Categories(Route):

    DEFAULTS = {
        'pageSize': 25,
        'format': 'json',
        'apiKey': '',
    }

    def __init__(self, settings):

        self.settings = Categories.DEFAULTS
        Route.__init__(self, settings)


    def search(self, params):

        params = self.format_params(params)
        endpoint = 'categories({params})'.format(params=params)
        url = self.get_full_url(endpoint)

        return self.execute(url)