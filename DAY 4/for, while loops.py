#for loop
#Next greater element

arr=eval(input('Enter an array: '))
target=int(input('Enter a target number: '))
arr.sort()
for i in range(len(arr)):
  if (arr[i]>target):
    print('Next greater element than the target element:',arr[i])
    break

#while loop
#count even and odd numbers

arr=eval(input('Enter an array: '))
i=0
odd_count,even_count=0,0
while i<len(arr):
  if (arr[i]%2==0):
    even_count+=1
  else:
    odd_count+=1
  i+=1
print('Even numbers count: ',even_count)
print('Odd numbers count: ',odd_count)