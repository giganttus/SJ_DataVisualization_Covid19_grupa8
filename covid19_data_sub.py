import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

data = pd.read_csv('static_data_sms.csv')
data['Date'] = pd.to_datetime(data['Date'])
x = data['Date']
y1 = data['San']
y2 = data['Mask']
y3 = data['Symp']

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.autofmt_xdate()
ax1.plot(x, y1, color='red', label='jedan')
ax2.plot(x, y2, color='green')
ax3.plot(x, y3, color='blue')
ax1.fill_between(x, y1, color='red', alpha=0.25)
ax2.fill_between(x, y2, color='green', alpha=0.25)
ax3.fill_between(x, y3, color='blue', alpha=0.25)
ax1.title.set_text('SREDSTVO ZA DEZINFEKCIJU')
ax2.title.set_text('MASKA')
ax3.title.set_text('COVID19 SIMPTOMI')


plt.tight_layout()
plt.show()
