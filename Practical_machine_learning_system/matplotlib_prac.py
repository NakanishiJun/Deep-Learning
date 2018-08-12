# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
