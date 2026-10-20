class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = [0] * 26

        if len(s) != len(t):
            return False

        for x in s:
            dif = ord(x) - ord('a')
            characters[dif] += 1
        
        for x in t:
            dif = ord(x) - ord('a')
            characters[dif] -= 1

        for char in characters:
            if char != 0:
                return False
            
        return True