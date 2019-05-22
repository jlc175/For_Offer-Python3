# 时间换空间，不使用辅助数组，时间复杂度为O(nlogn),空间复杂度为O(1)


# 统计值在star to end内的数字个数
def countRange(numbers, start, end):
    count = 0
    for number in numbers:
        if number >= start and number <= end:
            count += 1
    return count


def getDuplicate(numbers):
    start = 1
    end = len(numbers) - 1
    while end >= start:
        middle = (end - start) // 2 + start
        # 统计在start to middle之间的数字数目
        count = countRange(numbers, start, middle)
        # 当end与start相等时，若当前值的个数大于一，则找到一个重复的数字
        if end == start:
            if count > 1:
                return start
            else:
                break
        # start to middle范围的值的数目大于它应有的数目时，在该范围继续寻找，否则到middle+1 to end的范围继续寻找
        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return None


if __name__ == "__main__":
    case1 = [1, 2, 3, 1]
    case2 = [1, 2, 3, 3, 2]
    case3 = []

    print('一个重复元素的情况', getDuplicate(case1))
    print('多个重复元素的情况', getDuplicate(case2))
    print('无元素的情况', getDuplicate(case3))
