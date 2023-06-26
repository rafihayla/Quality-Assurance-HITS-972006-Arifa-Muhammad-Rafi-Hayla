# https://leetcode.com/problems/distinct-subsequences/solutions/1472969/python-bottom-up-dp-explained/

class Solution:
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] += dp[i-1][j] 			#if current character is skipped
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]	#if current character is used
        
        return dp[-1][-1]

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    result = Solution().numDistinct(S, T)
    print(result)
