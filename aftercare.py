# aftercare
import pandas as pd
from datetime import datetime
import random



def update_records(starttime,
                   r,
                   inter,
                   sessionprofit,
                   sessionincrease,
                   startBalance,
                   endBalance,
                   fd,
                   fe):

    df = pd.read_csv('ops.csv')

    now = datetime.now()
    elap = now - starttime
    
    starttime = starttime.strftime("%d/%m/%Y %H:%M")
    now = now.strftime("%d/%m/%Y %H:%M")

    
    mylist = ["start datetime",
              "end datetime",
              "elapsed time",
              "reps",
              "interval",
              "numerical profit",
              "percentage profit",
              "starting bankroll",
              "end end bankroll",
              "fd s",
              "fe s"]
    toadd = {"start datetime":starttime,
              "end datetime":now,
              "elapsed time":elap,
              "reps":r,
              "interval":inter,
              "numerical profit":sessionprofit,
              "percentage profit":sessionincrease,
              "starting bankroll":startBalance,
              "end end bankroll":endBalance,
              "fd s":fd,
              "fe s":fe}

    #df=pd.DataFrame(columns=mylist) #this resets the spreadsheet....
    #never use this... its basically a self distruct button
    df = df.append(toadd,ignore_index=True)
    df.to_csv("ops.csv")

