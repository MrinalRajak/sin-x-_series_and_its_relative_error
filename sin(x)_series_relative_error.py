

#Relative error for sine series

import math as m
x=float(input("Enter the value of x in degrees: "))
x=m.radians(x)
t=x
i=1;s=t;j=0;s1=0
while(abs(s1-s)/abs(s)>1.0e-8):
    s1=s
    deno=(i+1.)*(i+2.)
    t=-t*(m.pow(x,2)/(deno))
    s=s+t
    i=i+2
    j=j+1

print("The Actual value is: ",m.sin(x))
print("The computed result is: ",s)
print("The no.of iteration: ",j)
print("The sum upto last but one term: ",s1)
