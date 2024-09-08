import pandas as pd


config=pd.read_excel("1h.xlsx")
config.set_index('time',inplace=True)
print(config)