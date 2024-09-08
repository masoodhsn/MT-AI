import pandas as pd
from scipy.interpolate import  interp1d as i1d
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


data=pd.read_excel("1h.xlsx")
data.set_index('time',inplace=True)

data=data.loc[:,['open']]

#print(data)


#################################
#برای هر دو نقطه کنار هم یک برازش انجام می دهد (درواقع همون پیدا کردن یک خط از دو نقطه است)مفید نیست
f=i1d(data.index,data['open'],kind='linear')

#################################
#تابعی که می خام روی آن برآزش انجام دهیم
def fu(x,a,b,c):
    return a*x*x+b*x+c

popt,pcov=curve_fit(fu,data.index,data['open'])
a,b,c=popt

#################################



plt.plot(data.index,data['open'],'o',label='data')
plt.plot(range(1725472800,1725656400),f(range(1725472800,1725656400)),label='i1d')
plt.plot(range(1725472800,1725656400),fu(range(1725472800,1725656400),a,b,c),label='curve fit')
plt.legend()
plt.show()