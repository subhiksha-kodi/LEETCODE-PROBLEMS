n=int(input())
ch=65
for i in range(n):
  for j in range(n-i):
    print(' ',end='')
  for j in range(i+1):
    print(chr(ch),end=' ')
  print('\n')
  ch+=1