from products import Products

class BestBuyAPI(object):

    def __init__(self, settings):

        # self.key = 'rqz7wj87qg4968s5hdaev3sc'
        self.settings = settings


    def products(self, params):

        products = Products(self.settings)
        response = products.search(params)
        
        return response['products']