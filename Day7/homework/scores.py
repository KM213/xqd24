"""
从一个包含学生姓名及三门课程成绩的文件中提取出每个人的成绩并将其总成绩放在该行末尾
文件内容格式：
        姓名1 课程1 课程2 课程3
        姓名2 课程1 课程2 课程3
"""
def sum_score():
    with open("score1.txt", 'r+') as f:
        lists = f.readlines()
        print(lists)
        for i in range(len(lists)):
            lists[i] = lists[i].strip('\n')
            lists[i] = lists[i].split()
            lists[i].append(str(int(lists[i][1]) + int(lists[i][2]) + int(lists[i][3])))
            lists[i] = " ".join(lists[i]) + '\n'

    with open("score2.txt", 'w+') as f:
        f.writelines(lists)
if __name__ == '__main__':
    sum_score()