from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = Counter(s1)
        to_match = len(h1.keys())
        matched = 0

        if len(s1) > len(s2): return False

        window_len = len(s1)
        h2 = {}

        for r in range(len(s2)-1):
            char = s2[r]
            # print(f"Adding {char}, h2={h2}")
            h2[char] = h2.get(char, 0) + 1

            if char in h1 and h1[char]==h2[char]:
                matched+=1
                
            l = r-(window_len)

            if l>=0:
                to_remove_char = s2[l]
                h2[to_remove_char]-=1
                # print(f"Removing {to_remove_char}, h2={h2}")

                if to_remove_char in h1 and h2[to_remove_char]==h1[to_remove_char]-1:
                    matched-=1
                    
            if matched==to_match:
                return True
        
        return False

            
# print(Solution().checkInclusion("ab","eidbaooo"))