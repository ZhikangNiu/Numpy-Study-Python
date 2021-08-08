import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])
# stack 沿着新的轴加入一系列数组。axis = 0等价于vstack。axis =1 等价于hstack
a1 = np.stack((a,b),axis=0)
print(a1)
# vertical stack 上下合并
c = np.vstack((a,b))
print("vertical stack: \n",c)
# horizontal stack
d = np.hstack((a,b))
print("horizontal stack:\n",d)
# [1,1,1]--->[[1][1][1]] 这步操作需要添加维度
a_newaxis = a[:,np.newaxis]
b_newaxis = b[:,np.newaxis]
c_hstcak = np.hstack((a_newaxis,b_newaxis))
print(a_newaxis.shape)
print(b_newaxis.shape)
print("horizontal stack:\n",c_hstcak)
# 指定axis进行操作，axis = 0是上下，axis = 1是左右
C = np.concatenate((a_newaxis,b_newaxis,a_newaxis),axis = 0)
print("concatenate:\n",C)