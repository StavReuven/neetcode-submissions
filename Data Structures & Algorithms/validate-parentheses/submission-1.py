class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {}
        table['}'] = '{'
        table[')'] = '('
        table[']'] = '['
        for ch in s:
            if ch not in table:
                stack.append(ch)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if table[ch] != cur:
                    return False
        return not stack