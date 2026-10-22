class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        cur = set()
        ans = 0
        while right < len(s):
            if s[right] in cur:
                cur.remove(s[left])
                left += 1
                continue
            cur.add(s[right])
            ans = max(right - left + 1, ans)
            right += 1
        return ans