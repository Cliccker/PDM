import numpy as np


def EuclideanDistance(x, y):
    d = 0
    # zip将两个列表打包为元组的列表
    for a, b in zip(x, y):
        d += (a - b) ** 2
    return d ** 0.5


def EuclideanDistance_np(x, y):
    # np.linalg.norm 用于范数计算，默认是二范数，相当于平方和开根号
    return np.linalg.norm(np.array(x) - np.array(y))


def Cosine(x, y):
    sum_xy = 0
    num_x = 0
    num_y = 0
    for a, b in zip(x, y):
        sum_xy += a * b
        num_x += a ** 2
        num_y += b ** 2
    if num_x == 0 or num_y == 0:  # 判断分母是否为零
        return None
    else:
        return sum_xy / (num_y * num_x) ** 0.5


def Cosine_np(x, y):
    a = np.array(x)
    b = np.array(y)
    d = np.linalg.norm(a) * np.linalg.norm(b)
    # 由于余弦相似度属于(-1,1)，这里进行归一化操作使最后的结果属于(0,1)
    return 0.5 + 0.5 * (np.dot(a, b) / d)


def Pearson(x, y):
    sum_xy = 0
    num_x = 0
    num_y = 0
    avr_x = sum(x) / len(x)
    avr_y = sum(y) / len(y)
    for a, b in zip(x, y):
        sum_xy += (a - avr_x) * (b - avr_y)
        num_x += (a - avr_x) ** 2
        num_y += (b - avr_y) ** 2
    if num_x == 0 or num_y == 0:  # 判断分母是否为零
        return None
    else:
        return sum_xy / (num_y * num_x) ** 0.5


def Pearson_np(x, y):
    a = np.array(x)
    b = np.array(y)
    # .corrcoef()是numpy中内置的计算皮尔逊相关系数的方法，同时需要进行归一化处理
    return 0.5 + 0.5 * (np.corrcoef(a, b, rowvar=0)[0][1])


def AdjCosine(x, y):
    sum_xy = 0
    num_x = 0
    num_y = 0
    for a, b in zip(x, y):
        avr = (x[0] + y[0]) / 2  # 计算第一项的均值
        sum_xy += (a - avr) * (b - avr)
        num_x += (a - avr) ** 2
        num_y += (b - avr) ** 2
    if num_x == 0 or num_y == 0:  # 判断分母是否为零
        return None
    else:
        return 0.5 + 0.5 * (sum_xy / ((num_y * num_x) ** 0.5))


def AdjCosine_np(x, y):
    a = np.array(x)
    b = np.array(y)
    avr = (x[0] + y[0]) / 2
    d = np.linalg.norm(a - avr) * np.linalg.norm(b - avr)
    return 0.5 + 0.5 * (np.dot(a - avr, b - avr) / d)


def AdjCosine_np_2(x, y):
    a = np.array(x)
    b = np.array(y)
    avr = np.mean(np.append(a, b, axis=0))  # 合并矩阵并求矩阵的平均值
    d = np.linalg.norm(a - avr) * np.linalg.norm(b - avr)
    return 0.5 + 0.5 * (np.dot(a - avr, b - avr) / d)


def Manhattan(x, y):
    d = 0
    for a, b in zip(x, y):
        d += a - b
    return abs(d)  # 取绝对值


def Chebyshev(x, y):
    d = np.array(x) - np.array(y)
    return np.max(np.maximum(d, -d))  # np.maximum(a, -a)这一步相当于在取绝对值

V_x = [1, 2, 3]
V_y = [1, 4, 100]
V_z = [2, 4, -7]
print(AdjCosine_np(V_x, V_y))  # 3
print(AdjCosine_np(V_x, V_z))  # 10
