class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0 (as per problem conventions)
        if not needle:
            return 0
        
        # Loop through haystack up to a point where needle can still fit
        for i in range(len(haystack) - len(needle) + 1):
            # Check if substring matches
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If not found, return -1
        return -1
