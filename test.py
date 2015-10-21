from psu import mkdir, ls, cd, touch

path = './test'
print(mkdir(path))
print(cd(path))
print(touch('x'))
print(ls('.'))
