from products import Products
from reviews import Reviews

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


    