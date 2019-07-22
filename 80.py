class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return n
        else:
            index = 2
            for i in range(2, n):
                if nums[i] != nums[index - 2]:
                    nums[index] = nums[i]
                    index += 1
                print(index, i+1, nums[:index], nums)
            return index


if __name__ == '__main__':
    nums1, ans1 = [1, 1, 1, 2, 2, 3], 5
    nums2, ans2 = [0, 0, 1, 1, 1, 1, 2, 3, 3], 7
    s = Solution()
    assert s.removeDuplicates(nums1) == ans1
    print()
    assert s.removeDuplicates(nums2) == ans2
