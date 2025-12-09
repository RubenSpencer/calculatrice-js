a = True + True + False

print(a , type(a))  # Output: 2 <class 'int'>

b = False + False + False
print(b , type(b))  # Output: 0 <class 'int'>

c = True * 10 + False * 5
print(c , type(c))  # Output: 10 <class 'int'>

d = (True + False) * (True + True)
print(d , type(d))  # Output: 2 <class 'int'>

e = True - False + True
print(e , type(e))  # Output: 2 <class 'int'>

f = False * 100 + True
print(f , type(f))  # Output: 1 <class 'int'>

g = True 
print(g , type(g))  # Output: True <class 'bool'>

h = False
print(h , type(h))  # Output: False <class 'bool'>