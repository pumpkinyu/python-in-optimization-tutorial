# A concise python code based tutorial for (mathmatical) optimization
# https://github.com/sorayng/python-in-optimization-tutorial
# Contact: Sean Yang - yng(at)outlook.com

# Task 2 - Newton's method for finding a minimum
# Date: 2014.01.13
# Description:
# 1. This routine tries to find a minimum of a single-variable nonlinear
#    equation, taking f(x) = 0.6*x**5 + x**4 - 30*x for example.
# 2. Newton's method iteratively uses second order Taylar approximation to find
#    better guess of the root, i.e,
#    min f(x) = f(x0) + f'(x0)(x - x0) + 1/2*f''(x0)(x - x0)**2 --->
#    x = x0 - f'(x0)/f''(x0)
# 3. For detailed reference, see http://en.wikipedia.org/wiki/Newton's_method
# 4. Notice that at x* where f'(x*) = 0, x* is a minimum when f''(x*) > 0 and is
#    a maximum when f''(x*) < 0.
# 5. The result x* of Task 2 should be the same as Task 1, because the function
#    used in Task 1 is the derivative of the one used in Task 2.

def func(x):
    ''' define the nonlinear equation '''
    return 0.6*x**5 + x**4 - 30*x

def funcgrad(x,h=1e-3):
    '''
    Caculate the derivative of f(x), using two-point finite difference formula:
    f'(x) = (f(x + h) - f(x - h))/2h
    More information of numerical differentiation, see
    http://en.wikipedia.org/wiki/Numerical_differentiation
    '''
    return (func(x + h) - func(x - h))/2/h

def funcgrad2(x,h=1e-3):
    ''' calculate the second order derivative of f(x) '''
    return (funcgrad(x + h) - funcgrad(x - h))/2/h

def find_a_minimum_newton(x0=100):
    '''
    Use Newton's method to find a minimum, x0 is the initial guess.
    '''
    print(x0)
    x = x0
    while abs(funcgrad(x)) > 1e-6:
        x = x - funcgrad(x)/funcgrad2(x)
        print(x)
    return x
    
if __name__ == '__main__':
    root = find_a_minimum_newton()
