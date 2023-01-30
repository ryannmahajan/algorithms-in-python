def find_sec_largest(nums):
    largest, sec_largest = max(nums[0], nums[1]), min(nums[0], nums[1])

    for num in nums[0:]:
        if num > largest:
            largest, sec_largest = num, largest
        elif num > sec_largest and num!=largest:
            sec_largest = num
    
    return sec_largest

print(find_sec_largest([99, 99, 58, 45, 82, 70]))