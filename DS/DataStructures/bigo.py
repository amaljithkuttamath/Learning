import matplotlib.pyplot as plt
import datetime

def linear(a,x,b, n):
    poly = a*x + b 
    ploting=[]
    for n in range(n):
        y = poly*n
        ploting.append(y)
    return ploting


r = []
for n in range(1000):    
    ss = datetime.datetime.utcnow()
    o = linear(a=10,x=10,b=10, n=n)
    st = datetime.datetime.utcnow()
    lol = [st - ss]
    r.append(lol)
# dat.stop
print(r)
# plt.plot(o)
# plt.show()