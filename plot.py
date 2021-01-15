import numpy as np
from matplotlib import pyplot as plt
import scipy.io as scio
from numpy.random.mtrand import randn

ys = 200 + np.random.randn(2, 100)
x = [x for x in range(len(ys[0]))]

# plt.plot(x, ys, 'b')
# plt.show()
plt.plot(x, ys[0], '-')
plt.fill_between(x, ys[0], 195, where=(ys[0]>195), facecolor='g', alpha=0.6)
plt.show()
# path = r'D:\Users\Pcd\Documents\WeChat Files\ch1en66\FileStorage\File\2021-01\data\Test_0018'
# data = scio.loadmat(path)
# print("你好，世界")


# for z in range(len(ys)):
#     print("你好，世界", z)

def testmethod(name, age=23, *args):
    """打印任何传入的字符串"""
    print("Name:", name)
    print("Age:", age)
    print("args:", type(args), args)
    for arg in args:
        print(arg)
    return

# testmethod(name="haha1", age=24)
# # testmethod(name="haha1", age=24, args = (1, 2, 3))
# testmethod("haha1", 24, (1, 2, 3))


def plot(*args, scalex=True, scaley=True, data=None, **kwargs):
    """ 看下参数情况 """
    print("*args:", args)
    print("*kwargs:", kwargs)
    pass

# plot(x, ys[0], '-', x, ys[1], 'r', linewidth=2, color='blue', markersize=13)

n1 = np.empty((3, 2))
n2 = np.empty([3, 2])

print('n1:', n1, 'n2:', n2)

for month in range(0, 12):
    print('month:', month)\

n1.reshape(1, -1)
