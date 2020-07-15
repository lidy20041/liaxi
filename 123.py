# _*_ coding uft _*_
# 开发环境：腾达建设
# 开发人员：Administrator
# 开发时间：2020-07-15  20:12
# 文件名称：123.py
# 开发工具：PyCharm


import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)

y1 = x * 2 + 100

y2 = x ** 2

# 创建一个画布

# figsize：设置画布的大小
plt.figure(figsize=(2, 2))
plt.plot(x, y1)

# 创建第二个画布
plt.figure()
plt.plot(x, y2)

plt.show()