class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagS = {}
        anagT = {}
        for i in range(len(s)):
            anagS[s[i]] = 1 + anagS.get(s[i], 0)
            anagT[t[i]] = 1 + anagT.get(t[i], 0)
        return anagS == anagT