class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        rev_num = 0
        temp = x

        while temp != 0:
            mod = temp % 10
            rev_num = rev_num * 10 + mod
            temp //= 10
        return rev_num == x