class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ret = ""
        for str in strs:
            ret += f"{len(str)}:{str}"
        
        return ret

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        ret = []

        i = 0
        while i < len(str):
            length = get_num_at(i, str)
            i += len(str(length)) + 1

            ret += str[i:i+length]
            i += length
        
        return ret

def get_num_at(i, str):
    num_string = ""
    for char in str[i:]:
        if char!=":":
            num_string += char
        else:
            break
    
    return int(num_string)