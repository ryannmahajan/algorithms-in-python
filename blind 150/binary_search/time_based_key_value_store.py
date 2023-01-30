class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr_list = self.d.get(key, None)
        if curr_list is None:
            self.d[key] = curr_list = []
        
        curr_list.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        return self.bin_search(self.d[key], timestamp)

    def bin_search(self, curr_list, timestamp):
        l, r = 0, len(curr_list) - 1

        while (l <= r):
            left = curr_list[l]
            if l==r:
                return get_val(left) if get_timestamp(left) <= timestamp else ""
            
            m = (l+r)//2
            mid = curr_list[m]

            if timestamp < get_timestamp(mid):
                r = mid
            elif get_timestamp(mid) <= timestamp < get_timestamp(curr_list[mid+1]):
                return get_val(mid)
            else:
                l = mid + 1

def get_val(node):
    return node[0]

def get_timestamp(node):
    return node[1]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)