#armstrong number
import math
n=int(input())
sum=0
copy=n
count=int(math.log10(n)+1)
while(n!=0):
  a=n%10
  sum+=(a**count)
  n//=10

if (copy==sum):
  print('Armstrong number')
else:
  print('Not an armstrong number')