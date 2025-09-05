#fibonacci

n=int(input())
a,b=0,1
if (n==0 | n==1):
  print(0)
if (n>=2):
  print(a,b,end=' ')
for i in range(2,n):
  c=a+b
  a=b
  b=c
  print(c,end=' ')