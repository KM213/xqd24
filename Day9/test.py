def reverseBits(n: int) -> int:
        # 进制转换 + 字符串填充
        # 进制转换 + 字符串填充
        num = bin(n)[2:].rjust(32, '0')
        # num = num[::-1]
        num = int(num[::-1], 2)
        return int(num)

def sum(nums, target):
    hashtable = dict()
    for index, num in enumerate(nums):
        print(index, num)
        if target - num in hashtable:
            return [hashtable[target - num], index]
        hashtable[nums[index]] = index
        print(hashtable)
    return []

if __name__ == '__main__':
    # 1. 二进制翻转
    print(reverseBits(15))
    # 2. 两数之和
    print(sum([1, 4, 6, 7, 8, 9], 10))