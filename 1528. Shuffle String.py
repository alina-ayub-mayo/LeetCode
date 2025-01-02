class Solution(object):
    def restoreString(self, s, indices):
        res = ""
        for i in range(len(s)):
            temp = indices.index(i)
            res = res + s[temp]
        return res
        