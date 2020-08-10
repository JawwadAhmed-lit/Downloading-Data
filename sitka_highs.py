import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    
# for index,coloumn in enumerate(header):
#     print(index,coloumn)

    time,highs = [] , []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        pop = int(row[5])
        time.append(current_date)
        highs.append(pop)
#print(highs)

# data visualistaion for hight temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(time,highs,c= 'red')

#setting
ax.set_title("Daily temperature " , fontsize = 24)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('HIGH TEMPERATURES (F)', fontsize = 16)
ax.tick_params(axis ='both', which ='major' , labelsize = 16)

plt.show()