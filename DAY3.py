#arrays, strings, for loop

#Next greater element (arrays)
arr=eval(input('Enter a integer array: '))
target=int(input('Enter a target number: '))
arr.sort()
for i in range(len(arr)):
  if (arr[i]>target):
    print('Next greater element of the target element:',arr[i])
    break

#count occurrence of a given character
s=input('Enter a string: ')
chr=input('Enter a character: ')[0]
count=s.count(chr)
print(count)