#recursion

def names(n,name):
  if (n<2):
    return name
  return name+' '+names(n-1,name)
n=int(input())
name=input()
print(names(n,name))