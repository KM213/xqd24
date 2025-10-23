# 0-1背包
def bag01(bag , goods):
    values = [[0 for _ in range(bag+1)] for _ in range(len(goods)+1)]
    for g in range(1, len(goods)+1):
        for b in range(1, bag + 1):
            if goods[g-1][0] <= b:
                values[g][b] = max(values[g-1][b-goods[g-1][0]] + goods[g-1][1],values[g-1][b])
            else:
                values[g][b] = values[g-1][b]
    return values



if __name__ == '__main__':
    bag = 6
    goods = [[1, 2], [2, 4], [3, 3]]
    print(bag01(bag, goods))



# import sys
#
#
#
# bag, m = map(int, input().split())
# vwq = []
# values = [[0 for _ in range(bag+1)] for _ in range(m +1)]
# for line in sys.stdin:
#     t = line.split()
#     t[1] = str(int(t[0]) * int(t[1]))
#     vwq.append(t)
# for g in range(1, m+1):
#     for b in range(1, bag+1):
#         if vwq[g-1][0] < bag:
#             pass
#         else:
#             values[g][b] = values[g-1][b]