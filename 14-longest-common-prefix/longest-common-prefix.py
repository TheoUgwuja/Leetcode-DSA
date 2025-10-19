class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        car0 = []

        if not strs:
            return ""

        limit = min(len(s) for s in strs)
        i = 0

        while i < limit:
            ch = strs[0][i]
            for s in strs:
                if s[i] != ch:
                    return "".join(car0)
            car0.append(ch)
            i += 1

        return "".join(car0)