#check for prime
n=int(input())
flag=1
if (n<2): 
  print('Not Prime')
  exit()
for i in range(2,n):
  if (n%i==0):
    flag=0
    break
if flag:
  print('Prime')
else:
  print('Not Prime')