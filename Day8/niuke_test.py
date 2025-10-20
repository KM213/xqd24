# 升序
def partation0(nums, left, right):
    i = left
    m = int(nums[right])
    for j in range(left, right):
        if int(nums[j]) <= m:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

# 降序：
def partation1(nums, left, right):
    i = left
    m = int(nums[right])
    for j in range(left, right):
        if int(nums[j]) >= m:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i

# 递归
def qsort(nums, left, right, flag):
    if left < right:
        if flag:
            i = partation1(nums, left, right)
        else:
            i = partation0(nums, left, right)
        qsort(nums, left, i-1, flag)
        qsort(nums, i+1, right, flag)
    print(f"qsort:{nums}")
    return nums

n = int(input())
nums = input().split()
flag = int(input())
# print(flag, type(flag))
li = qsort(nums, 0, n-1, flag)
for i in li:
    print(i, end=" ")