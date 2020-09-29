import numpy as np
import matplotlib.pyplot as plt

for i in range(len(xv)):
    yv[i] = np.sqrt(3*xv[i]-2)
for i in range(len(xv)):
    yv1[i] = yv[i]*-1

plt.plot(xv, yv,'-b')
plt.plot(xv, yv1,'-b')
x = np.linspace(-10,10,500)
y2=(23/24)-(2*x)
plt.annotate("(41/48,-3/4)", (41/48, -3/4))
plt.plot(x,y2,'r')
plt.xlim(-10,20)
plt.ylim(-5,5)
plt.grid()
plt.show()
