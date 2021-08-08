import numpy as np
from numpy.random import random

# 构建矩阵
# 创建的向量都是行向量
A = np.array([1,2,3])
B = np.array([[1,2,3],[4,5,6]])
# numpy的几种属性:ndim,shape,size
# ndim 返回的是矩阵的维度
print('number of dim:',A.ndim)
print('number of dim:',B.ndim)
# shape 返回的是矩阵的大小，可以使用shape属性或者np.shape()的方法进行
print('shape of array:(property):',A.shape)
print('shape of array:(function):',np.shape(A))
print('shape of array:(property):',B.shape)
print('shape of array:(function):',np.shape(B))
# size访问的是矩阵里面的元素数目
print('number of items:',A.size)
print('number of items:',B.size)
print("---------------------------------------")
# 指定数据dtype
a = np.array([2,3,4],dtype='int64')
print('a dtype:',a.dtype)
# int 64
b = np.array([2,23,4],dtype='int32')
print('b dtype:',b.dtype)
# int32
c = np.array([2,23,4],dtype='float64')
print('c dtype:',c.dtype)
# float64
d = np.array([2,23,4],dtype='float32')
print('d dtype:',d.dtype)
# float32
print("---------------------------------------")
# 构建全0矩阵 --> (3,2) =3 x 2的全0矩阵
C = np.zeros((3,2))
print(C)
print("---------------------------------------")
# 构建全一矩阵
D = np.ones((3,2))
print(D)
print("---------------------------------------")
# 构建无限接近于0的数组
E = np.empty((3,3))
print(E)
print("---------------------------------------")
# 用arange创建连续数组,(start,end,step) ---> [start,end)
# 创建一个从1开始到9结束，步长为2的数组
F = np.arange(1,10,2)
print(F)
print("---------------------------------------")
# 创建线段，[start,end]
# 开始端1，结束端6，且分割成6个数据，生成线段
G = np.linspace(1,6,6)    
print(G)
print("---------------------------------------")
# 改变矩阵的大小 --> (1 X 6)-->(2 X 3)
H = G.reshape((2,3))
print(H)
print("---------------------------------------")
# 创建随机数组
# 设置随机数的种子，确保每次复现都是一样的
np.random.seed(10)
I = np.random.random((3,2))
print(I)
print("---------------------------------------")
# 访问数组元素
data = np.array([1,2,3,1])
# 证明基于值管理内存
print(id(data[0])==id(data[3]))
# 访问元素
print(data[1])
# 切片还是左开右闭
# 切片访问
print(data[0:2])
print(data[1:])