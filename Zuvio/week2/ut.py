import numpy as np
x = np.ones([3, 4])
print(x,'\n')
y = x.reshape([4, 3])
print(y,'*\n')
z= y+1
print(z,'\n')
h=np.random.randint(50, size=(4,3))
print(h,'$\n')
g = z[0:2,0]+2*h[1:3,1]
print(z[0:2,0])
print(2*h[1:3,1])
print(g,'\n')
b = z[0:2,0:2]+2*h[1:3,1:3]
print(z[0:2,0:2])
print(2*h[1:3,1:3])
print(b,'~\n')
