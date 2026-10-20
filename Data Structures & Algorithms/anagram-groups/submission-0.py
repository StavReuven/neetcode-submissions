class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for str in strs:
            word = [0]*26
            for char in str:
                word[ord(char) - ord('a')] += 1
            wordS = tuple(word)
            groups[wordS].append(str)
        return list(groups.values())