from math import *
a=int(input('введите коэффициент a: '))
b=int(input('введите коэффициент b: '))
c=int(input('введите коэффициент c: '))
d=b**2-4*a*c
if d<0:
    print('нет решений')
if d==0:
    print('x=',-b/(2*a))
if d>0:
    print('x1=',(-b+sqrt(d))/(2*a),'\nx2=',(-b-sqrt(d))/(2*a))