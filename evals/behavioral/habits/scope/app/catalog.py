PRODUCTS={ 'basic':{'price':10,'name':"Basic"} , 'pro':{'price':25,'name':"Pro"} }
def price_of(key):
  return PRODUCTS[key]['price']
