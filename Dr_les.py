#Дремучий лес
import math

def f(x, a):                         
  l1=((1-a)**2+x**2)**0.5
  l2=(a**2+(1-x)**2)**0.5
  t=t=l1/vp+l2/vr
  return t

l=0
r=1
EPS = 1e-6
vp, vr=map(int, input().split())
a=float(input())    
while r - l > EPS:
  x1 = (l * 2 + r) / 3
  x2 = (l + r * 2) / 3
  if f(x1, a)>f(x2, a):
    l=x1
  else:
    r=x2
print((l + r) / 2) 
