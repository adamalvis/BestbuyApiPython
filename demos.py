from bestbuyapi import BestBuyAPI

def product_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
        'show': 'customerReviewAverage,sku,name,longDescription'
    })

    products = bb.products({
                   'categoryPath.id': 'abcat0507008',
                   'customerReviewAverage>': '3'
               })

    return products


def review_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    reviews = bb.reviews({
            'sku': '7008759',
        })

    return reviews


def store_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    stores = bb.stores({
            'postalCode': '33510',
        })

    return stores


def category_search():

    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    categories = bb.categories({
            'id': 'abcat0507008',
        })

    return categories