class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [len(s) + 1]

        dp[-1] = True
        STR_LENGTH = len(s)

        for i in range(STR_LENGTH-1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if (i+word_len <= STR_LENGTH) and s[i:i+word_len]:
                    dp[i] = dp[i+word_len]
                
                if dp[i]: break

        return dp[0]
