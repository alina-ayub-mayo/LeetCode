class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
            
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if it's the start of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
