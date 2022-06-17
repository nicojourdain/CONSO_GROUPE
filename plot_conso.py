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
print(dates)
print(xdates)
print(conso_groupe)

#-------------------------------------------------

#ax = plt.gca()
fig, ax = plt.subplots()

formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
ax.xaxis.set_major_locator(locator)

plt.plot(xdates,alloc_groupe)
plt.plot(xdates,conso_groupe)


#-------------------------------------------------
fig.savefig('conso_gen6035.jpg')
