import numpy as np
from numpy.core.fromnumeric import ptp
from numpy.core.numeric import ones
from numpy.core.records import array

data = np.array([1,2])
ones = np.ones(2)
print('---------------------------')
# 两矩阵相乘，乘以所对应的数字
print("ones*data: ",ones*data)
# 两矩阵相加
print("data+ones: ",data+ones)
# 两矩阵相减
print("data-ones: ",data-ones)
# 两矩阵相除数
print("data/data: ",data/data)
# 矩阵乘以常数
print("data*1.6: ",data*1.6)
# 矩阵平方
print("data square: ",data**2)
print('---------------------------')
data = np.array([1,2,3,4,5])
# 求最大值
print("data max: ",data.max())
# 求最小值
print("data min: ",data.min())
# 求和
print("data sum: ",data.sum())
print('---------------------------')
# broadcast机制
data = np.array([[1,2],[3,4],[5,6]])
print("data shape: ",data.shape)
print("data is :",data)
ones_row = np.array([1,1])
print(ones_row.shape)
print(ones_row+data)
# --------------------
# [1,1]---->[[1,1],[1,1],[1,1]]再相加
print('---------------------------')
data = np.array([1,2,3])
# (1 x 3)
powers_of_ten = np.array([[1,10],[100,1000],[10000,100000]]) 
# (3 x 2)
print(data.dot(powers_of_ten))
# (1 x 2)
print('---------------------------')
# 二维矩阵的操作
data = np.array([[1,2],[3,4],[5,6]])
# 矩阵转置
print("transpose ",data.T)
# 求最大值
print("max is :",data.max())
# 求最小值
print("min is :",data.min())
# 求和
print("sum is: ",data.sum())
# 输出data的shape
print("shape is: ",data.shape)
# 将data行向量的维度由3行塌为1行
print("column max is: ",data.max(axis=0))
# 将data列向量的维度由2列塌为1列
print("row max is: ",data.max(axis=1))
# 求均值
print("mean is:",data.mean())
# 索引操作
print("data[0,1] is:\n\t",data[0,1])
print("data[1,3] is:\n",data[1:3])
print("data[0:2,0] is:\n\t",data[0:2,0])
print('---------------------------')
# 更高维的操作
data = np.array([[[1,2],[0,4]],[[5,6],[7,8]]])
print("shape: ",data.shape)
# 将元素展开
print("flatten: ",data.flatten())
# 返回的是最大值和最小值的索引
print("the index of min: ",np.argmin(data))
print("the index of max: ",np.argmax(data))
# 函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵
print(np.nonzero(data))
# 将行，列，维度这些三维坐标返回
row,column,dim = np.nonzero(data)
# 创建A矩阵，逆序
A = np.arange(14,2, -1).reshape((3,4)) 

# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(A))    
# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])