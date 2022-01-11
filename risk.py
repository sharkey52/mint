# risk aversion
import execution
import random

def standev(df):
    # calculate standard deviation of prices so
    # we can come up with take profit and stop loss 
    pass
def randkiller(r):
    if str(r)[-1] == '0':
        execution.close_all()
    else:
        pass

def killlosers():
    import tpqoa
    oanda = tpqoa.tpqoa('oanda.cfg')
    if float(oanda.get_account_summary()['unrealizedPL']) < 0:
        execution.close_all()
    else:
        pass


def random_risk(order,df):
    
    diff = (df.iloc[-1].loc['h'])-(df.iloc[-1].loc['l'])

    if order['signal'] == 'buy':
        order['sl'] = (df.iloc[-1].loc['l']) - diff
        order['tp'] = (df.iloc[-1].loc['h']) + 2*diff
    elif order['signal'] == 'sell':
        order['sl'] = (df.iloc[-1].loc['h']) + diff
        order['tp'] = (df.iloc[-1].loc['l']) - 2*diff
    
    return order

def r_decider(order,df):
    
    mylist = [random_risk]
    order = random.choice(mylist)(order,df)
    return order
