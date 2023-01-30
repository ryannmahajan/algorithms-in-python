from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)

        