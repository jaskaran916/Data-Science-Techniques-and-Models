import pandas as pd
import statsmodels.graphics.tsaplots as tsa_plots
import statsmodels.api as sm


import os
os.getcwd()

Amtrak = pd.read_csv("Amtrak.csv")
Amtrak.rename(columns={"Ridership ('000)":"Ridership"},inplace=True)  

tsa_plots.plot_acf(Amtrak.Ridership,lags=12)
tsa_plots.plot_pacf(Amtrak.Ridership,lags=12)


model1 = sm.tsa.arima.ARIMA(Amtrak.Ridership,order=(1,1,1)).fit()
model2=  sm.tsa.arima.ARIMA(Amtrak.Ridership,order=(12,1,7)).fit()
model1.summary()
model1.aic
model2.aic

p=1
q=0
d=1
pdq=[]
aic=[]
for q in range(7):
    try:
        model=sm.tsa.arima.ARIMA(Amtrak.Ridership,order=(p,d,q)).fit()

        x=model.aic

        x1= p,d,q
               
        aic.append(x)
        pdq.append(x1)
    except:
        pass
            
keys = pdq
values = aic
d = dict(zip(keys, values))
print (d)
