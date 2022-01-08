# main
import data
import alpha
import risk
import portfolio
import execution
import watchlist
import tpqoa
import time
import random
import pandas as pd

print('Starting...:',end='')

port = pd.DataFrame()

oanda = tpqoa.tpqoa('oanda.cfg')
startBalance = oanda.get_account_summary()['balance']

r = 0
def repcounter(r):
    r = r + 1
    print(r,end='|')
    return r

if 1==1:#__name__ == '__main__':
    while r < 5000:
        try:
            time.sleep(25)
            order = {'ticker':'GBP_USD'}
            if 1==1:
                #portfolio.checkin(port,order):
                df = data.get_data()
                # order = alpha.machlearn(order,df)
                order = alpha.a_decider(order,df)
                #order = r_decider(order,df) # this wont work after ml because it got rid of high and low
                risk.killlosers()
                order = portfolio.p_decider(order)
                #print('-------------------')
                #print(order)
                r = repcounter(r)
                
            #order = watchlist.scorecard(order) #this needs testing
            try:
                execution.run(order)
                port = execution.add_to_port(order,port)
            except:
                print('FE',end='|')
        except:
            print('FD', end='|')

execution.close_all()
endBalance = oanda.get_account_summary()['balance']
sessionprofit = float(endBalance[:8]) - float(startBalance[:8])
sessionincrease = (100 / float(startBalance[:4])) *sessionprofit
print(sessionprofit)
print(str(sessionincrease)[:4] + '%')
print('end')
