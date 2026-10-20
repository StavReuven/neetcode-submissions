class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st = st + s + chr(257)
        return st
    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        for ch in s:
            if ch == chr(257):
                res.append(cur)
                cur = ""
                continue
            cur += ch
        return res