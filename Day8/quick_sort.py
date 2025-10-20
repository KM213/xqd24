# 分区函数 - 将数组重新排列，返回基准的最终位置
def partation(nums, low, high):
    print(f"分区：{nums[low:high+1]}")
    pivot = nums[high]      # 选择基准（这里选择最右边的元素）
    i = low                  # 初始化指针i, i指向小于基准的子数组的边界位置。初始为 low，表示初始小于基准的元素区域长度为0
    print(f"初始值：low = {low},high = {high}, i = {i},pivot = {pivot}")
    for j in range(low, high):      # 遍历子数组（从 low 到 high-1），high作为基准不参与遍历
        print(f"比较前：i = {i},j = {j},nums = {nums}")
        if nums[j] <= pivot:        # 如果当前元素 nums[j] 小于或等于基准
            nums[i], nums[j] = nums[j], nums[i]  # 交换元素，将当前小于基准的元素 nums[j] 放到边界i的位置
            i += 1      # 小于基准的区域向右扩展一位
        print(f"比较后：i = {i},j = {j},nums = {nums}")
    nums[i], nums[high] = nums[high], nums[i]       # 放置基准到正确位置: 将基准元素放到分界位置
    print(f"一轮分区结束：i = {i},j = {j},nums = {nums}")
    return i    # 返回基准的最终位置

# 原地快速排序 - 不创建新列表，直接在原数组上操作
def qsort(nums, low, high):     # nums: 待排序的列表   low: 当前子数组的起始索引   high: 当前子数组的结束索引
    if low < high:      # 递归条件：子数组长度大于等于1
        i = partation(nums, low, high)      # 分区操作，返回基准元素的最终位置
        print(f"左递归：{nums[low:i]}")
        qsort(nums, low, i-1)               # 递归排序左半部分（基准左边的元素）
        print(f"右递归：{nums[i+1:high+1]}")
        qsort(nums, i+1, high)              # 递归排序右半部分（基准右边的元素）
    print("递归完成")
    # 递归出口：子数组为空，即 low > high

if __name__ == '__main__':
    nums = input().split()
    qsort(nums, 0, len(nums) - 1)
    for i in nums:
        print(i, end=" ")