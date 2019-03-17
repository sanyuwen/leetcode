"""
数组中选第k大数字？ follow up :  如果只能使用最多w内存空间呢？
"""
import heapq
import random


def k_largest(k, nums):
    """
    :param k: int >0
    :param nums: [int]
    :return: k th largest number in the array
    assume: len(nums)>=k
    """
    h = nums[:k]
    heapq.heapify(h)
    for num in nums[k:]:
        if h[0] < num:
            heapq.heappushpop(h, num)
    return h[0]


if __name__ == '__main__':
    upper_bound = 100
    case = 10
    for i in range(case):
        nums = list(range(upper_bound))
        rint = random.randint(1, upper_bound - 1)
        random.shuffle(nums)
        assert k_largest(rint, nums) == sorted(heapq.nlargest(rint, nums))[0]
