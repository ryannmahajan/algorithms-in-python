import re

class Solution:
    def convert_string(s):
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        return s.lower()

    def isPalindrome(self, s: str) -> bool:
        s = self.convert_string(s)
        length = len(s)

        if length==0: return True
        for i in range(length):
            if i>=length-i-1: break

            if s[i]!=s[length - 1 - i]:
                return False
            
        
        return True