class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Step 1: remove all non-alphanumeric characters
        step1 = ""
        for ch in s:
            if ch.isalnum():
                step1 += ch

        # Step 2: lowercase
        step2 = step1.lower()

        # Edge case
        if len(step2) <= 1:
            return True

        # Convert to list
        step2list = list(step2)

        # Halfway point
        z = len(step2) // 2

        # Palindrome check
        for i in range(0, z, 1):
            if step2list[i] != step2list[-(i+1)]:
                return False
        
        return True
