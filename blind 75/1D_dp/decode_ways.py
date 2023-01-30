class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        first = 1 if s[0]!='0' else 0
        if len(s) == 1: return first

        second = (1 if is_char(s[0:2]) else 0) + (first if s[1]!='0' else 0)
        if len(s) == 2: return second

        for i in range(2, length):
            first, second = second, (second if s[i]!='0' else 0) + (first if is_char(s[i-1:i+1]) else 0)
        
        return second

def is_char(str):
    return 10 <= int(str) <= 26