class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   #the last seen index of each character 
        left = 0        # the left side of the sliding window 
        max_len = 0    # the max length found so far
        
        for right, char in enumerate(s):  # move the right pointer through the string 
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # Move left pointer past the duplicate
            
            
            char_index[char] = right # Update the last seen index of the current character
            
            
            max_len = max(max_len, right - left + 1) # Update max length of substring without repeating any characters
        
        return max_len
