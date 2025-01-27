import numpy as np
import matplotlib.pyplot as plt
from funcs import * # 如果这一行报错，删掉
import math
# 记得 cmd运行： pip install numpy matplotlib

# 设置x的范围和精度
x = np.linspace(0, 10, 40000)  # 从0到10，生成40000个点

def func1(x): # 你自己写；**是乘方，math.log(x, b)是对数函数，x是自变量，b是底数，不填就是e
    return 1670000 * 0.946 ** (10 * x - 48)

# 计算对应的y值
y = []
plt.title("P")
for i in x:
    y.append(func1(i)) # func1 是你的函数
y=np.array(y)


# 绘制图像
plt.plot(x, y, label="1670000 * 0.946 ** (10 * x - 48)")  # 修改label为你的函数表达式

# 添加标题和标签

plt.xlabel("x")
plt.ylabel("y")

# 添加图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图像
plt.show()