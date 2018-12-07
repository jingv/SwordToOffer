# coding:utf-8

s = 'we are happy.'

# print(s.replace(' ', '%20'))

s = '%20'.join(s.split(' '))
print(s)
