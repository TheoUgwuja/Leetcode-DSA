class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = (s.rsplit())      #define splitted as the split version of string
        return(len(splitted[-1]))  #returns the len of the last word in the list 