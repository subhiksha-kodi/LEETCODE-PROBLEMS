#recursion

def number(n):
  if n<2:
    return n
  return n*number(n-1)

n=int(input())
print(f'Product: {number(n)}')