#recursion

def numbers(n):
  if (n<1):
    return 
  print(n,end=' ')
  numbers(n-1)

n=int(input())
numbers(n)