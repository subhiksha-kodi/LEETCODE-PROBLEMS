#if else statement

#Entered character is vowel,consonant,special character
chr=input('Enter a character: ')
chr_lower=chr.lower()
if chr_lower in 'aeiou':
  print(chr,'is a vowel')
elif chr_lower.isalpha():
  print(chr,'is a consonant')
else:
  print(chr,'is a special character')

#switch case 

#Simple calculator
a=int(input('Enter a: '))
b=int(input('Enter b: '))
oper=input('Enter operations to be perform: ')
match oper:
  case '+':
    print('Sum of',a,'and',b,':',a+b)
  case '-':
    print('Difference of',a,'and',b,':',a-b)
  case '*':
    print('Product of',a,'and',b,':',a*b)
  case '/':
    if b!=0:
      print('Division of',a,'and',b,':',a/b)
    else:
      print('Zero division error')
  case _:
    print('Invalid')