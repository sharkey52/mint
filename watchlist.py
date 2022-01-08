# watchlist

s = 0
def scorecard(order):
    s = s + 1
    if str(s)[-1] == '0':
        if order == 'buy':
            order['signal'] = 'sell'
            order['units'] = score
        elif order == 'sell':
            order['signal'] = 'buy'
            order['units'] = score
        else:
            pass
    else:
        if order == 'buy':
            score = score + 10
        elif order == 'sell':
            score = score - 10
        else:
            pass
    return order
