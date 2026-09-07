from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup = {}

        for word in strs:
            gimatria = sum(ord(char) for char in word)
            if gimatria not in anagramGroup:
                anagramGroup[gimatria] = []
            anagramGroup[gimatria].append(word)
        
        result = []
        for gimatria, words in anagramGroup.items():
            subGroup = {}
            for word in words:
                countWord = tuple(sorted(Counter(word).items()))
                if countWord not in subGroup:
                    subGroup[countWord] = []
                subGroup[countWord].append(word)
        
            for group in subGroup.values():
                result.append(group)
        
        return result