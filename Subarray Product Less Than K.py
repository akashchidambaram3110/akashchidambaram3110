class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        i = 0
        ans = 0

        for j in range(len(nums)):
            product *= nums[j]

            while product >= k:
                product /= nums[i]
                i += 1

            ans += (j - i + 1)

        return ans
