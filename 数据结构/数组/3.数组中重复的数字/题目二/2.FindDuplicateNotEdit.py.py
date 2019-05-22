def getDuplicate(numbers):
    # 初始化辅助数组
    auxiliary = [None for i in range(len(numbers))]
    for number in numbers:
        if auxiliary[number] != None:
            return number
        auxiliary[number] = number
    return None


if __name__ == "__main__":
    case1 = [1, 2, 3, 1]
    case2 = [1, 2, 3, 3, 2]
    case3 = []

    print('一个重复元素的情况', getDuplicate(case1))
    print('多个重复元素的情况', getDuplicate(case2))
    print('无元素的情况', getDuplicate(case3))