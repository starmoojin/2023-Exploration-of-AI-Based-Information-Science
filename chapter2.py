import sys
a=7
b=3.7
c=a
# print(type(a), type(b))
# print(id(a), id(b), id(c))
print(f'{sys.getrefcount(a)}')
c='school'
print(f'{sys.getrefcount(a)}')
