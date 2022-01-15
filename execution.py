import pandas as pd
import time
import tpqoa

oanda = tpqoa.tpqoa('oanda.cfg')

#order = {'ticker': 'GBP_USD', 'alpha': 'moving_av', 'signal': 'buy', 'sl': 1.1307199999999997, 'tp': 1.1326000000000005, 'port': 'port', 'units': 20}

def run(order):
    ticker = order['ticker']
    
    #creates a buy order from order dictionary if the signal is buy
    if order['signal'] == 'buy': 
      oanda.create_order(instrument = 'GBP_USD',units=order['units'],suppress=True, ret=True)

      
    #creates a buy order from order dictionary if the signal is sell
    if order['signal'] == 'sell': 
      oanda.create_order(instrument = 'GBP_USD',units=-order['units'],suppress=True, ret=True)

def add_to_port(order,portfolio):
    
    portfolio = portfolio.append(order,ignore_index=True)

    return portfolio

def close_all():
    if oanda.get_positions() == []:
        pass
    else:
        longpos = oanda.get_positions()[0]['long']['units']
        shortpos = oanda.get_positions()[0]['short']['units']
        longpos = float(longpos)
        shortpos = float(shortpos)
        if longpos != 0.0:
            oanda.create_order(instrument = 'GBP_USD',units=-longpos,suppress=True, ret=True)
        elif shortpos != 0.0:
            oanda.create_order(instrument = 'GBP_USD',units=-shortpos,suppress=True, ret=True)
        else:
            print('please manually check all positions are closed...')
            print('my execution.close_all() function fucked up!!! ')


