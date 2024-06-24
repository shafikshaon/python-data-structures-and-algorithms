class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        feq_map = {}
        for i in range(len(s)):
            if s[i] in feq_map:
                feq_map[s[i]] += 1
            else:
                feq_map[s[i]] = 1

            if t[i] in feq_map:
                feq_map[t[i]] -= 1
            else:
                feq_map[t[i]] = -1

        for char in feq_map:
            if feq_map[char] != 0:
                return False
        return True


sol = Solution()
s1 = "listen"
t1 = "silent"
print(sol.isAnagram(s1, t1))
