# A concise python code based tutorial for (mathmatical) optimization
# https://github.com/sorayng/python-in-optimization-tutorial
# Contact: Sean Yang - yng(at)outlook.com

# Task 1 - Newton's method for finding a root
# Date: 2014.01.10
# Description:
# 1. This routine tries to find a root of a single-variable nonlinear equation,
#    taking f(x) = 3*x**4 + 4*x**3 - 30 for example.
# 2. Newton's method iteratively uses first order Taylar approximation to find
#    better guess of the root, i.e,
#    f(x) = f(x0) + f'(x0)(x - x0) = 0 --->
#    x = x0 - f(x0)/f'(x0)
# 3. For detailed reference, see http://en.wikipedia.org/wiki/Newton's_method

def func(x):
    ''' define the nonlinear equation '''
    return 3*x**4 + 4*x**3 - 30

def funcgrad(x,h=1e-3):
    '''
    Caculate the derivative of f(x), using two-point finite difference formula:
    f'(x) = (f(x + h) - f(x - h))/2h
    More information of numerical differentiation, see
    http://en.wikipedia.org/wiki/Numerical_differentiation
    '''
    return (func(x + h) - func(x - h))/2/h

def find_a_root_newton(x0=100):
    '''
    Use Newton's method to find a root, x0 is the initial guess.
    '''
    print(x0)
    x = x0
    while abs(func(x)) > 1e-6:
        x = x - func(x)/funcgrad(x)
        print(x)
    
if __name__ == '__main__':
    find_a_root_newton()
