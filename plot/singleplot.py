# coding=utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


np.random.seed(1000)
y = np.random.standard_normal(10)
plt.plot(y.cumsum())
plt.grid(True) ##增加格点
plt.axis('tight') # 坐标轴适应数据量 axis 设置坐标轴
plt.show()