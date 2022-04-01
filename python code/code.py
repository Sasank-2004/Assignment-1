import numpy as np
from math import sqrt
from matplotlib import pyplot as plt


def f(x):
     return (2*x+sqrt(4*x**2-1))/(2*x-sqrt(4*x**2-1))


x = np.linspace(0.5,2,num=100)
y = [f(i) for i in x]
y1 = [4 for i in range(100)]
plt.xlabel("X axis ")
plt.ylabel("Y axis")
plt.title("My first Graph")
plt.grid()
plt.plot(x,y,label = 'y=f(x)')
plt.plot(x,y1,label = 'y=4')
plt.annotate("(0.625,4)",(0.625,4),(0.7,15),arrowprops={"arrowstyle":"<-"})
plt.show()

if f(5/8)==4:
     print("Correct Answer")
else :
     print("Wrong Answer")
