class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        l, r = 0, m - 1
        while True:
            i = (l + r) // 2  # the mid index for nums1
            j = half - i - 2  # the corresponding index for nums2
            
            # Edge handling
            Aleft = nums1[i] if i >= 0 else float('-inf')
            Aright = nums1[i + 1] if (i + 1) < m else float('inf')
            Bleft = nums2[j] if j >= 0 else float('-inf')
            Bright = nums2[j + 1] if (j + 1) < n else float('inf')
            
            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total lengths
                if total % 2:
                    return min(Aright, Bright)
                # Even total lengths
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
