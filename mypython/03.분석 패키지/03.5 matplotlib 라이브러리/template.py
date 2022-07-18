import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

filename = 'seriesGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + ' 파일 저장')
