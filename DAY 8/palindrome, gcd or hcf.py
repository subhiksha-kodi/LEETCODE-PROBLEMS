#palindrome
n=int(input())
str_n=str(n)
rev_n=int(str_n[::-1])
if (n==rev_n):
  print('Palindrome')
else:
  print('Not a palindrome')

#gcd or hcf
import math
a=int(input())
b=int(input())
res=math.gcd(a,b)
print(res)

#OR

a=int(input())
b=int(input())
while b!=0:
  a,b=b,a%b
print(a)