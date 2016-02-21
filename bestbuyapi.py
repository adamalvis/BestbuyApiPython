from products import Products
from reviews import Reviews
from stores import Stores

class BestBuyAPI(object):

    def __init__(self, settings):
        self.settings = settings


    def products(self, params):

        products = Products(self.settings)
        response = products.search(params)
        
        return response['products']


    def reviews(self, params):

        reviews = Reviews(self.settings)
        response = reviews.search(params)

        return response['reviews']


    def stores(self, params):

        stores = Stores(self.settings)
        response = stores.search(params)

        return response['stores']


