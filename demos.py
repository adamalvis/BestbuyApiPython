from bestbuyapi import BestBuyAPI

def product_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    products = bb.products({
                   'categoryPath.id': 'abcat0507008', # motherboards category
               })

    return products

def review_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    reviews = bb.reviews({
            'sku': '7008759'
        })

    return reviews