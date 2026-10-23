class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        seen = {}
        output = 0
        maxf = 0

        for right in range(len(s)):
            ch = s[right]
            seen[s[right]] = seen.get(ch, 0) + 1
            maxf = max(maxf, seen[ch])
            while (right - left + 1) - maxf > k:
                seen[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output
