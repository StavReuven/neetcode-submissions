class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        sep = chr(257)
        for s in strs:
            st = st + s + sep
        return st
    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        sep = chr(257)
        for ch in s:
            if ch == sep:
                res.append(cur)
                cur = ""
                continue
            cur += ch
        return res