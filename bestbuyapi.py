from product_search import ProductSearch

class BestBuyAPI(object):

    def __init__(self, settings):

        # self.key = 'rqz7wj87qg4968s5hdaev3sc'
        self.settings = settings


    def product_search(self, params):

        product_search = ProductSearch(self.settings)
        response = product_search.search(params)
        
        return response['products']