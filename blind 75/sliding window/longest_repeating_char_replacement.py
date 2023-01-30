class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        LENGTH = len(s)
        l, r = 0, 0

        freq = {}
        max_char = None

        while (r < LENGTH):
            char = s[r]

            freq[char] = freq.get(char, 0) + 1
            max_char = set_new_max_char(max_char, char, freq)

            while is_decreasing_needed(freq, max_char, k) and l<=r:
                freq[s[l]] -=1
                if s[l]==max_char:
                    max_char = set_new_max_char_by_checking_all_others(max_char, freq)

                l+=1

            max_len = max(max_len, freq[max_char] + k)
        
        return min(max_len, LENGTH)

def is_decreasing_needed(freq, max_char, k):
    return (sum(v for k,v in freq if k!=max_char) > k)

def set_new_max_char(max_char, char, freq):
    if max_char is None or freq[char] > freq[max_char]:
        return char
        
    return max_char
    
def set_new_max_char_by_checking_all_others(max_char, freq):
    curr_max_freq = freq[max_char]
    for k, v in freq.items():
        if v>curr_max_freq:
            max_char = k
            curr_max_freq = v
    
    return max_char
