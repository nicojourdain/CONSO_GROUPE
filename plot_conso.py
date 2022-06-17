import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

f = open('consommation_proj_gen6035.txt', 'r')

Nline=0
for line in f:
  Nline=Nline+1
f.seek(0) # rewind

conso_groupe=np.zeros((Nline))
alloc_groupe=np.zeros((Nline))

dates=[]
kdate=0
for line in f:
    line = line.strip()
    columns = line.split()
    dates = np.append(dates,columns[0])
    conso_groupe[kdate] = float(columns[1])
    alloc_groupe[kdate] = float(columns[2])
    kdate=kdate+1

f.close()

#xdates=np.datetime64(dates)
xdates = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in dates]

d0=datetime.datetime.strptime('2022-05-01',"%Y-%m-%d").date()
nb_day_alloc=np.zeros((Nline))
for kdate in np.arange(Nline):
  delta=xdates[kdate]-d0
  nb_day_alloc[kdate] = delta.days

#-------------------------------------------------

#ax = plt.gca()
fig, ax = plt.subplots()

formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)

#locator = mdates.DayLocator()
#ax.xaxis.set_major_locator(locator)

plt.plot(xdates,alloc_groupe,color='k',linewidth=2.0)
plt.plot(xdates,alloc_groupe*nb_day_alloc/365.,'--',color='grey',linewidth=1.2)
plt.plot(xdates,conso_groupe,color='grey',linewidth=1.8)


#-------------------------------------------------
fig.savefig('conso_gen6035.jpg')
