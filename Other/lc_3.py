""" Given a string s, find the length of the longest
substring
without repeating characters. """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SubStringLength = 0
        CharSet = set()
        l = 0
        for r in range(len(s)):
            #if current character is not in set, add it right side and check if new max substring length
            if s[r] not in CharSet:
                CharSet.add(s[r])
                SubStringLength = max(SubStringLength, r - l + 1)
            # if it is in set, remove characters left side until it is not
            else:
                while s[r] in CharSet:
                    CharSet.remove(s[l])
                    l +=1
                CharSet.add(s[r])
            
        
        return SubStringLength
