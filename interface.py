import PySimpleGUI as sg
import matplotlib.pyplot as plt
import time

import mplfinance as mpf
import pandas as pd
import yfinance as yf
li = ['red','orange','teal']
mc = mpf.make_marketcolors(up='g',
                           down='r',
                           edge='lime',
                           wick={'up':'blue','down':'orange'},
                           volume='darkred',
                           ohlc='red')
mystyle  = mpf.make_mpf_style(base_mpf_style='nightclouds',
                        marketcolors=mc,mavcolors=li,
                        facecolor='black',
                        edgecolor='#800000',
                        figcolor='black',
                        gridcolor='#4b0082',
                        gridstyle='dotted',
                        gridaxis='vertical',
                        y_on_right = False)

#numbers = yf.download('AAPL',period='1d',interval='5m')
#numbers = pd.DataFrame(numbers)


def tillchristmas():
    till = 4904
    return till

def authentication():

    layout = [[sg.Text('Personal key:')],
              [sg.InputText(key='kpass')],
              [sg.Text('Perminent password:')],
              [sg.InputText(key='ppass')],
              [sg.Text('Dynamic password:')],
              [sg.InputText(key='dpass')],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window('this is window title',layout)

    event, values = window.read()
    window.close()

    till = tillchristmas()
    till = str(till)
    passcode = 'password'
    name = values['kpass']
    name = name.upper()
    ppass = str(values['ppass'])
    dpass = str(values['dpass'])
    

    if ppass == passcode:
        if dpass == till:
            print('Hello ' + name, end=' ')
            return True
        
        else:
            return False
    else:
        return False

def graphit(numbers):
    layout = [[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup')]]

    window = sg.Window('Have some Matplotlib....', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Plot':
            mpf.plot(numbers,
             type='candle',
             mav=(25,10,30),
             volume=True,
             show_nontrading = True,
             style=mystyle,
             tight_layout=True,
             figratio=(25,10),
             figscale=0.8)
        elif event == 'Popup':
            sg.popup('Yes, your application is still running')
    window.close()

def counter():
    BAR_MAX = 1000

    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
              [sg.Cancel()]]

    window = sg.Window('Custom Progress Meter', layout)
    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['-PROG-'].update(i+1)
        
    window.close()
        
counter()
