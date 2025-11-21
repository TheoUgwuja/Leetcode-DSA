class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start = 0
        end = 0  # indices of best palindrome so far
        
        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now just outside the palindrome
            return left + 1, right - 1
        
        for i in range(len(s)):
            # odd-length palindrome (center at i)
            l1, r1 = expand_from_center(i, i)
            # even-length palindrome (center between i and i+1)
            l2, r2 = expand_from_center(i, i + 1)
            
            # pick the longer of the two
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]
