# function_retun_even_no

def count_evens(nums):
    count = 0
    len_nums = len(str(nums))
    list_nums = list(str(nums))

    for element in range(len_nums):
        list_nums1 = list_nums[element]
        if int(list_nums1) % 2 == 0 or int(list_nums1 == 0):
            count += 1
    return count


print(count_evens(687478568))
