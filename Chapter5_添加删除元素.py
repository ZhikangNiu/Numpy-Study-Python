import numpy as np

# numpy.resize 函数返回指定大小的新数组。
#如果新数组大小大于原始大小，则包含原始数组中的元素的副本。

a = np.array([[1,2,3],[4,5,6]])
print (a)
# 未超出原始大小
b = np.resize(a, (3,2))
print (b)
# 超出原始大小时，包含副本
b = np.resize(a,(3,3))
print (b)

# append()添加元素在末尾，一定保证中括号[]数目一致
print(np.append(a,[[1,1,1]],axis=0))
print(np.append(a,[[1],[1]],axis=1))

# insert 给定索引前面插入
# 未传递 Axis 参数。 在插入之前输入数组会被展开
a = np.array([[1,2],[3,4],[5,6]])
print(np.insert(a,2,[11,12]))
# 传递axis参数进去
print(np.insert(a,2,[11,12,10],axis=1))
print(np.insert(a,2,[11,12],axis=0))

# delete 删除元素
# umpy.delete 函数返回从输入数组中删除指定子数组的新数组。 
# 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开
a = np.array([[1,2],[3,4],[5,6]])
print(np.delete(a,1))
print(np.delete(a,1,axis=1))
print(np.delete(a,1,axis=0))

#numpy.unique
#numpy.unique 函数用于去除数组中的重复元素。
a = np.array([5,2,6,2,7,5,6,8,2,9])
print (a)
print ("remove repeated value:",np.unique(a))
u,indices = np.unique(a, return_index = True)
print ("after removing,the value original index:",indices)


u,indices = np.unique(a,return_inverse = True)
print (u)
# 重复元素在旧数组中的索引
print(indices)
print(u[indices])
# 计数
print ('every item number after removing repeated number:')
u,indices = np.unique(a,return_counts = True)
print ("item: ",u)
print ("count:",indices)