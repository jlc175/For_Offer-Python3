def getDuplicate(numbers):
    # 初始化辅助数组
    auxiliary = [None for i in range(len(numbers))]
    for number in numbers:
        if auxiliary[number] != None:
            return number
        auxiliary[number] = number
    return None

if __name__ == "__main__":
    print(getDuplicate([1, 2, 3, 3]))
    print(getDuplicate([]))
    print(getDuplicate([1, 1, 2, 2]))
