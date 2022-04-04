import numpy as np
from math import sqrt
from matplotlib import pyplot as plt


def f(x):
     return (2*x+sqrt(4*x**2-1))/(2*x-sqrt(4*x**2-1))


x = []
y = []
with open("output.txt","r") as fp:
    for lines in fp :
        x.append(lines[0:8])
        y.append(lines[10:-1])
x.remove(x[0])
y.remove(y[0])
for i in range(len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])
x1 = np.linspace(0,4,num=100)
y1 = [4 for i in range(100)]
plt.xlabel("X axis ")
plt.ylabel("Y axis")
plt.title("My first Graph")
plt.grid()
plt.plot(x,y,label = 'y=f(x)')
plt.plot(x1,y1,label = 'y=4')
plt.annotate("(0.625,4)",(0.625,4),(0.7,15),arrowprops={"arrowstyle":"<-"})
plt.show()
if f(5.0/8==4):
     print("Correct Answer")
else :
     print("Wrong Answer")

