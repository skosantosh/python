mylist = [1, 1, 2, 4, 3]
# Make function to chack
# arrayCheck([1,1,2,3,1])->True 123 in sequence
# arrayCheck([1,1,2,4,1])-> False not in Sequence
# arrayCheck([1,1,2,1,2,3])-> True in Sequence


def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print(arrayCheck(mylist))
