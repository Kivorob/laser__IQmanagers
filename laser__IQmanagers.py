from pylab import *
import matplotlib as mpt
import matplotlib.pyplot as plt
import re
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
import math

def read(data):
    res = []
    sublist = []
    for i in data:
        sublist.append(i)
        if len(sublist) == 3:
            sublist[0] = int(sublist[0])
            sublist = tuple(sublist)
            res.append(sublist)
            sublist = []
    return res




fin = open('input.txt', 'r')
data = fin.read()
fin.close()
data = re.sub('[](,)[]', ' ', data)
data = list(map(float, data.split()))
res = read(data)
x, y = 0.0, 0.0
plt.figure(figsize=(35/2.54, 35/2.54))
plt.xticks(np.arange(-1100, 1100, 50))
plt.yticks(np.arange(-1100, 1100, 50))
plt.xlabel('x', fontsize=25)
plt.ylabel('y', fontsize=25)
xlim(-1100, 1100)
ylim(-1100, 1100)
#print(len(res))
for i in range(0, len(res)):
    if res[i][2] > 4000.0:
        res[i][2] = 4000.0
    elif res[i][2] < 5.0:
        res[i][2] = 5.0
    x = (round(res[i][2] * cos(radians(res[i][1]))))
    y = (round(res[i][2] * sin(radians(res[i][1]))))
    print("x = ", x, "y = ", y)
    plt.scatter(x, y, color='blue', s=res[i][0], marker='o')
plt.axhline(0, color='lightgrey', linestyle='-')
plt.axvline(0, color='lightgrey', linestyle='-')

show()
