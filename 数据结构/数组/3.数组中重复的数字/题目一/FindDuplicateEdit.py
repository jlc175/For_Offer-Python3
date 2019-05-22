def duplicate(nums):
    # 从头遍历数组
    for i in range(len(nums)):
        # 当前位置的数字不在它应该的位置
        while nums[i]!=i:
            # 如果当前位置的数字与它应该在的位置的数字相同，则找到了一对相同的数字
            if nums[i]==nums[nums[i]]:
                return nums[i]
            # 将当前数字放到它应该在的位置
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
    # 未找到相同的数字
    return False

if __name__ == '__main__':
    case1 = [2, 1, 3, 4, 3, 5]
    case2 = [2, 2, 3, 4, 3, 5]
    case3 = []
    
    print('一个重复元素的情况', duplicate(case1))
    print('多个重复元素的情况', duplicate(case2))
    print('无元素的情况', duplicate(case3))