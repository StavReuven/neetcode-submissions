class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = [0] * 128
        cur = [0] * 128
        left = 0
        leftI = 0
        rightI = 0
        maxr = float('inf')

        for i in range(len(t)):
            seen[ord(t[i])] += 1
        
        need = sum(1 for x in seen if x > 0)
        have = 0

        for right in range(len(s)):
            c = ord(s[right])
            cur[c] += 1
            if seen[c] > 0 and cur[c] == seen[c]:
                have += 1
            while have == need:
                if (right - left + 1) < maxr:
                    rightI = right
                    leftI = left
                    maxr = right - left + 1
                c = ord(s[left])
                cur[c] -= 1
                if seen[c] > 0 and cur[c] < seen[c]:
                    have -= 1
                left += 1

        if maxr == float('inf'):
            return ""
        return s[leftI: rightI + 1]

