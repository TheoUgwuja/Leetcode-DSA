class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num
        for ch in s:
            if ch != '0':
                min_num = int(s.replace(ch, '0'))
                break
        else:
            min_num = num
        return max_num - min_num
