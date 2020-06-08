import time
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.animation import FuncAnimation

plt.style.use('classic')

def animate(i):
    data = pd.read_csv('dynamic_data_sms.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    x = data['Date']
    y1 = data['San']
    y2 = data['Mask']
    y3 = data['Symp']

    plt.cla()
    plt.plot(x, y1, linewidth='1.5', color='red', label='\"Sredstvo za dezinfekciju\"')
    plt.plot(x, y2, linewidth='1.5', color='green', label='\"Maska\"')
    plt.plot(x, y3, linewidth='1.5', color='blue', label='\"Simptomi\"')

    plt.ylabel('Br. pretraga')
    plt.xticks(rotation=70)
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=500)
plt.title('Pretraživani pojmovi za vrijeme COVID19')

plt.tight_layout()
plt.show()

