class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Sort the list to get the expected heights
        expected = sorted(heights)
        
        # Initialize a counter for mismatches
        mismatch_count = 0
        
        # Compare each element of heights with the expected order
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
        
        # Return the number of mismatches
        return mismatch_count