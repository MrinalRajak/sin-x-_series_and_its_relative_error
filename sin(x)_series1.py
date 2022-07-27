

#Computing sum of sine series term by term addition

import math as m
x=float(input("Enter the value of x in degrees: "))
x=m.radians(x)
t=x
i=1;s=t;j=0
while(m.fabs(t)>1.0e-8):
    deno=(i+1.)*(i+2.)
    t=-t*(m.pow(x,2)/(deno))
    s=s+t
    i=i+2
    j=j+1

print("Actual value: ",m.sin(x))
print("Computed result: ",s)
print("The no.of iterations: ",j)
