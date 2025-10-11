from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits == [9]:                    
            return [1, 0]
        elif digits == [9, 9]:
            return [1, 0, 0]
        elif digits[-1] == 9:
            digits[-1] = 0
            i = len(digits) - 2
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                    i = i - 1
                else:
                    digits[i] = digits[i] + 1
                    return digits
            return [1] + digits
        else:
            temp = (digits[-1])
            temp = temp + 1
            digits.pop(-1)
            digits.append(temp)
            return (digits)




#rough work 
#return (digits[-1])
#return(digits)
#if digit == 9 append 1,0
#need to handle if last digit is 9 -> carry over
#like 1,9 should become 2,0
#and 9,9 should become 1,0,0