from bestbuyapi import BestBuyAPI

def product_search():
    bb = BestBuyAPI({
        'apiKey': 'rqz7wj87qg4968s5hdaev3sc',
    })

    print bb.product_search({
              'categoryPath.id': 'abcat0507008', # motherboards category
          })