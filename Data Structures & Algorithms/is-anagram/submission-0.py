class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        anagramDict = {}
        for letter in s:
            if letter not in anagramDict:
                anagramDict[letter] = 1
            else:
                anagramDict[letter] += 1
        for letter in t:
            if letter not in anagramDict or anagramDict[letter] == 0:
                return False
            anagramDict[letter] -= 1
        return True