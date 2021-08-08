import numpy as np

# 创建数组
a = np.arange(12).reshape((3,4))
print(a)
# 选定维度分割
print(np.split(a,3,axis=0))
print(np.split(a,4,axis=1))
# 不等分割
print(np.array_split(a,3,axis=1))
# horizontal split 左右分割
print(np.hsplit(a,4))
# vertiacl split 上下分割
print(np.vsplit(a,3))