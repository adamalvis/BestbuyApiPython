from routes.products import Products
from routes.reviews import Reviews
from routes.stores import Stores
from routes.categories import Categories

class BestBuyAPI(object):

    def __init__(self, settings):
        self.settings = settings


    def products(self, params):

        products = Products(self.settings)
        response = products.search(params)
        
        return response


    def reviews(self, params):

        reviews = Reviews(self.settings)
        response = reviews.search(params)

        return response


    def stores(self, params):

        stores = Stores(self.settings)
        response = stores.search(params)

        return response


    def categories(self, params):

        categories = Categories(self.settings)
        response = categories.search(params)

        return response
