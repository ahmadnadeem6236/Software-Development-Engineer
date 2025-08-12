# Two Pointers

# def twoSum(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]

#         if current_sum == target:
#             return True
#         elif current_sum < target:
#             left +=  1
#         elif current_sum > target:
#             right -= 1
#     else:
#         return False



# nums = [1,3,4,6,8,10,13]
# target = 6
# result = twoSum(nums, target)
# print(result)


def containsWater(nums):
    left, right = 0, len(nums) - 1
    current_max = 0

    while left < right:
        width = right - left
        height = min(nums[left], nums[right])
        current_area = width * height

        current_max = max(current_max, current_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return current_max

nums = [3,4,1,2,2,4,1,3,2]
result = containsWater(nums)
print(result)
