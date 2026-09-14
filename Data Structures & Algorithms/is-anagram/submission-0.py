class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = sorted(s)
        string2 = sorted(t)

        if(len(string1) != len(string2)):
            return False
        for i in range(len(string1)):
            if(string1[i] != string2[i]):
                return False
        return True
        