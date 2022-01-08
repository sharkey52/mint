# feature engineering

def signalbuilder(df):
    
    df = df.drop('complete',axis=1)
    df = df.drop('volume',axis=1)
    df = df.drop('h',axis=1)
    df = df.drop('l',axis=1)
    df['avg'] = df.mean(axis=1)

    df['-1'] = df.avg.shift(1)
    df['-2'] = df.avg.shift(2)
    df['-3'] = df.avg.shift(3)
    df['-4'] = df.avg.shift(4)
    df['-5'] = df.avg.shift(5)

    df['buy1'] = df.avg < df.avg.shift(-1)
    df['buy2'] = df.avg < df.avg.shift(-2)
    df['buy3'] = df.avg < df.avg.shift(-3)
    df['buy4'] = df.avg < df.avg.shift(-4)
    df['buy5'] = df.avg < df.avg.shift(-5)
    df = df.replace({True: 1, False: 0})
    df['result'] = df['buy1']+df['buy2']+df['buy3']+df['buy4']+df['buy5']
    df = df.drop('buy1',axis=1)
    df = df.drop('buy2',axis=1)
    df = df.drop('buy3',axis=1)
    df = df.drop('buy4',axis=1)
    df = df.drop('buy5',axis=1)
    df.loc[df.result == 0, 'result'] = 'sell'
    df.loc[df.result == 1, 'result'] = 'sell'
    df.loc[df.result == 2, 'result'] = 'no trade'
    df.loc[df.result == 3, 'result'] = 'no trade'
    df.loc[df.result == 4, 'result'] = 'buy'
    df.loc[df.result == 5, 'result'] = 'buy'

    df = df.drop('o',axis=1)
    df = df.drop('c',axis=1)

    return df



def moving_av(df,smol,big):
  df['mav1'] = df['o'].rolling(window=smol).mean()
  df['mav2'] = df['o'].rolling(window=big).mean()
  df['mavdiff'] = df['mav1'] - df['mav2']
  
  return df

def standard_dev(df,n):
  df['openDev'] = df['o'].rolling(n).std()
  df['volDev'] = df['volume'].rolling(n).std()
  return df

def vwap(df): # this doesnt work correctly and needs fixing
  df['PV'] = ((df['c']+df['l']+df['h'])/3)*df['volume']
  df['VWAP'] = df['PV']/df['volume']
  return df
