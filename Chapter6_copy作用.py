import numpy as np

# 由于Python是基于值的管理内存
a = np.arange(0,12).reshape((3,4))
print(a)
b = a
c = b
d = c
# 使用id进行内存的访问
print(id(d)==id(a))
# 对d进行改动
print(d[2,3])
# 对d的值进行改变
d[2,3]=21
print(d)
# 发现a,b,c的值也被改动了
print(a)
print(b)
print(c)
# 这样会导致牵一发而动全身，因此为了解决这种情况我们需要使用copy来进行操作
a = np.arange(0,12)
print(a)
b = a.copy()
b[3] = 11
# 发现a的值没有改变，b的值改变了，解决了我们的问题。我们需要根据实际情况进行选择是=还是copy
print(b)
print(a)