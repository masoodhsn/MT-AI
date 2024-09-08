import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd


def get_history():
    mt5.initialize()
  
    history = pd.DataFrame(mt5.copy_rates_from_pos('XAUUSD', mt5.TIMEFRAME_H1, 0,1000 ))

    history['time'] = pd.to_datetime(history['time'], unit='s')

    history.set_index('time', inplace=True)

    history=history.loc[:,['open','high','low','close','tick_volume']]
    
    history.to_excel('1h.xlsx')

    


get_history()