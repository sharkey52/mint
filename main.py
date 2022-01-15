# main
import data
import alpha
import risk
import portfolio
import execution
import watchlist
import aftercare
from datetime import datetime
import tpqoa
import time
import random
import pandas as pd

print('Starting...:',end='')
starttime = datetime.now()
port = pd.DataFrame()
inter = 2
repetitions = 20
fe = 0
fd = 0
oanda = tpqoa.tpqoa('oanda.cfg')
startBalance = oanda.get_account_summary()['balance']

r = 0
def repcounter(r):
    r = r + 1
    print(r,end='|')
    return r

if __name__ == '__main__':
    while r < repetitions:
        try:
            time.sleep(inter)
            order = {'ticker':'GBP_USD','sl':1,'tp':2}
            if 1==1:
                #portfolio.checkin(port,order):
                df = data.get_data()
                order = alpha.machlearn(order,df)
                #order = alpha.a_decider(order,df)
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
                fe = fe + 1
        except:
            print('FD', end='|')
            fd = fd + 1

execution.close_all()
endBalance = oanda.get_account_summary()['balance']
sessionprofit = float(endBalance[:8]) - float(startBalance[:8])
sessionincrease = (100 / float(startBalance[:4])) *sessionprofit

aftercare.update_records(starttime,
                   r,
                   inter,
                   sessionprofit,
                   sessionincrease,
                   startBalance,
                   endBalance,
                   fd,
                   fe)
print('end')
