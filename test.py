import os
os.chdir("web")
a = os.path.abspath(__file__)
b = a.find('test.py')
print(a[:b] + ' ' + a)
