#arrays
#print sum,min,max of a array and print the reversed array

arr=eval(input('Enter an array: '))
print('Sum of the array: ',sum(arr))
print('Maximum element in the array: ',max(arr))
print('Minimum element in the array: ',min(arr))
print('Reversed array: ',arr[::-1])

#strings
#count occurrence of a given character

s=input('Enter a string: ')
chr=input('Enter a character: ')[0]
count=s.count(chr)
print(count)