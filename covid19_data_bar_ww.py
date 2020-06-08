import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

data = pd.read_csv('world_data.csv')
tc = data['total_cases']
td = data['total_deaths']
tr = data['total_recovered']
ac = data['active_cases']

y = [tc[0], td[0], tr[0], ac[0]]

y_sorted = sorted(y)

colors = ['#f51818', '#18f518', '#18e6f5', '#818f84']
labels = ['Preminuli', 'Oporavljeni', 'Aktivni', 'Zaraženi']

x_pos = [i for i, _ in enumerate(labels)]

plt.bar(x_pos, y_sorted, color=colors, width=0.75)


plt.title('COVID19 - Globalno Stanje (Ukupno)')

plt.xticks(x_pos, labels)

plt.tight_layout()
plt.show()