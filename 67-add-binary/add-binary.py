class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Converts binary strings to integers, adds them, and converts the sum back to binary
        return bin(int(a, 2) + int(b, 2))[2:]
