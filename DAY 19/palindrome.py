#palindrome

str=input()
str_rev=str[::-1]
if (str==str_rev):
  print('Palindrome')
else:
  print('Not palindrome')