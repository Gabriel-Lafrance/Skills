import os,sys
from app.pricing import total
def summary( order ):
    return {'id':order['id'],'due':total(order['subtotal'],order.get('discount',0),order['tax_rate'])}
