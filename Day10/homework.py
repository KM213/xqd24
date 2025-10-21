"""
Day10
练习
"""
# 1. 找出1000以内所有能同时被3和7整除的数字并存入列表
print("1. 找出1000以内所有能同时被3和7整除的数字并存入列表")
list1 = [i for i in range(1000) if i % 3 ==0 and i % 7 == 0]
print(list1)

# 2. 找出1000以内的水仙花数 （水仙花数：N位数（n≥3），它的每个位上的数字的n次幂之和等于它本身）
print("2. 找出1000以内的水仙花数")
list2 = [i for i in range(100, 1000) if sum(int(j) ** len(str(i)) for j in str(i)) == i and len(str(i))]
print(list2)