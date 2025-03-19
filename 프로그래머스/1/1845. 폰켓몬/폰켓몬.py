def solution(nums):
    answer = 0
    len_num = len(nums) / 2
    nums = set(nums)
    len_set = len(nums)
    answer = min(len_set,len_num)
    return answer