#Program to solve ordinary differential equation of order n<=5 using Runge-Kutta Method of fourth order by Maciej Cichosz
import numpy
import matplotlib.pyplot
import sympy
#here the user needs to define the n-th derivative of sought function as a function of other derivatives, the function and a variable
#def f(x,y,d1y,d2y,d3y,d4y):

"""def f(x,dy):
    #print (dy)Y
    return 0*x-0.1*dy[1]
    #return numpy.float64(dy[1])**2-numpy.float64(dy[0])
#dy[i] is the (i)th derivative. dy[0] is the value of y."""

def strtof(expression):
    def function(x, dy):
        return eval(expression)
    return function




def Rungekutta(equation, order, step_size, step_number, init_conditions):

    #f=sympy.sympify(equation)
    f = strtof(equation)

    steps=step_number

    h=float(step_size)

    #The program uses initial conditions for the same x for all derivatives of the function y.
    x=[0]*(steps+1)

    x[0]=init_conditions[0]

    derivatives=numpy.zeros([order+1, steps+1])

    for i in range (0, order):
        derivatives[i,0]=init_conditions[i+1]


    f0=[0]*(order+1)
    f1=[0]*(order+1)
    f2=[0]*(order+1)
    f3=[0]*(order+1)
    fh=[0]*(order+1)

    derivatives[order][0]=0
    derivatives[order][0]=f(x[0],derivatives[:,0])

    for i in range (1,steps+1):
        x[i]=x[i-1]+h
        f0[order]=f(x[i-1],derivatives[:,i-1])
        for j in range (0,order+1):
            if j==0:
                f0[order-j] = f(x[i - 1], derivatives[:, i - 1])
            elif j==1:
                f0[order - j] = f(x[i - 1], derivatives[:, i - 1]) * h
            else:
                f0[order - j] = derivatives[order-j+1][i-1] * h

        for k in range(0, order + 1):
            fh[k] = f0[k] / 2

        for j in range(0, order + 1):
            if j == 0:
                f1[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh)
            elif j == 1:
                f1[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh) * h
            else:
                f1[order - j] = (derivatives[order - j + 1][i - 1] + f0[order - j + 1] / 2) * h

        for k in range(0, order + 1):
            fh[k] = f1[k] / 2

        for j in range(0, order + 1):
            if j == 0:
                f2[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh)
            elif j == 1:
                f2[order - j] = f(x[i - 1] + h / 2, derivatives[:, i - 1] + fh) * h
            else:
                f2[order - j] = (derivatives[order - j + 1][i - 1] + f1[order - j + 1] / 2) * h

        for k in range(0, order + 1):
            fh[k] = f2[k]

        for j in range(0, order + 1):
            if j == 0:
                f3[order - j] = f(x[i - 1] + h, derivatives[:, i - 1] + fh)
            elif j == 1:
                f3[order - j] = f(x[i - 1] + h, derivatives[:, i - 1] + fh) * h
            else:
                f3[order - j] = (derivatives[order - j + 1][i - 1] + f2[order - j + 1]) * h


        for j in range(0, order + 1):
            derivatives[order - j][i]=derivatives[order - j][i-1] + (f0[order - j] +2*f1[order - j] +2*f2[order - j] +f3[order - j])/6

    y=derivatives[0,:]
    z=derivatives[1,:]

    matplotlib.pyplot.plot(x,y)
    matplotlib.pyplot.plot(x,z)

    matplotlib.pyplot.show()