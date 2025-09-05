#recursion

def numbers(n,a):
  if (a>n):
    return
  print(a,end=' ')
  numbers(n,a+1)

n=int(input())
numbers(n,1)