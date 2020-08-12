#setting
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    
# for index,coloumn in enumerate(header):
#     print(index,coloumn)

    time,highs,lows = [] , []  , []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            pop = int(row[4])
            lop = int(row[5])
        except ValueError:
            print(f"Missinng data {current_date}")
        else:
            time.append(current_date)
            highC = ((pop-32)*5//9)
            lowC = ((lop-32)*5//9)
            highs.append(highC)
            lows.append(lowC)
#print(highs)

# data visualistaion for hight temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(time,highs,c= 'red', alpha =0.5)
ax.plot(time,lows,c = 'blue', alpha =0.5)
ax.fill_between(time, highs,lows , facecolor = 'blue', alpha= 0.1)
#setting
ax.set_title("Daily High and Low temperature " , fontsize = 24)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('HIGH And Low TEMPERATURES (C)', fontsize = 16)
ax.tick_params(axis ='both', which ='major' , labelsize = 16)

plt.show()