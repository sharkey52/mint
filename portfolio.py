# portfolio construction
import random

def checkin(port,order):
    print(port.ticker.to_string(index=False))
    return True
    

def random_port(order):
    
    order['port'] = 'port'
    order['units']=200#random.randint(10,80)*100
    
    return order

def p_decider(order): 
    order = random_port(order)
    return order


