class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        left = 0
        seen = [0] * 26
        cur = [0] * 26
        for i in range(len(s1)):
            seen[ord(s1[i]) - ord('a')] += 1

        for right in range(len(s2)):
            cur[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 > len(s1):
                cur[ord(s2[left]) - ord('a')] -= 1
                left += 1
            res = self.check(cur, seen)
            if res:
                return True
        return False


    def check(self, a1, a2) -> bool:
        for i in range(26):
                if a1[i] != a2[i]:
                    return False
        return True