#functions (call by reference)
#swap two numbers

a=int(input())
b=int(input())
def swap(a,b):
  a,b=b,a
  return a,b

print('Inside the function: ',swap(a,b))
print('Outside the function: ',a,b)

#functions (call by value)
#count no.of words in a sentence

def word_count(string):
  words=string.split()
  print('Word count: ',len(words))

word_count('Apple is a fruit')