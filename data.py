import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import tpqoa
import datetime

oanda = tpqoa.tpqoa('oanda.cfg')

def get_data():

    x = datetime.datetime.now()
    y = x - datetime.timedelta(days=1)
    stop=(str(x)[:17]+'00')
    start=(str(y)[:17]+'00')
    
    data = oanda.get_history(  
        instrument='EUR_USD',  
        start=start,  
        end=stop,  
        granularity='M1',  
        price='M'
        )
    return data

def showmethemoney(x):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    mpl.rcParams['lines.linestyle'] = '--'
    
    plt.plot(x,color='green',label='this is a line label')
    plt.plot(4,6,'ro',label='this is a red label')
    plt.plot(8,3,'ro')
    plt.plot([3,3], [6,6],'-ro')
    ax.legend()
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    #ax.annotate('pointy arrow', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
    
#x = [3,5,2,4,6,3,5,6,3,5,6,6]
#showmethemoney(x)
