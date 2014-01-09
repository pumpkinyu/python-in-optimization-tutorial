'''
1. 通过牛顿法求根，演示函数为func(x) = 3*x**4 + 4*x**3 - 30
2. 牛顿法通过函数在x0处的一阶泰勒展开找到更好的近似值，即：
    func(x) = func(x0) + func'(x0)*(x - x0)
    令func(x) = 0，解得x = x0 - func(x0)/func'(x0)
3. 导数的计算采用数值方法，使用五点法公式，即：
    func'(x0) = (func(x0-2h) - 8*func(x0-h) + 8*func(x0+h) - func(x0+2h))/(12*h)
    其中h为微分步长，程序里取h = 1e-3
4. 数值微分的方法可以参阅http://en.wikipedia.org/wiki/Numerical_differentiation
'''

def func(x):    # 定义函数
    return 3*x**4 + 4*x**3 - 30

def funcgrad(x):    # 求一阶导数
    h = 1e-3
    return (func(x-2*h) - 8*func(x-h) + 8*func(x+h) - func(x+2*h))/(12*h)

xval = 10    # 给定初值xval = 10
while abs(func(xval)) > 1e-6:
    xval = xval - func(xval)/funcgrad(xval)
    print(xval)
