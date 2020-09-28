# APPROACH 1: DYNAMIC PROGRAMMING
# Time Complexity : 
# Space Complexity : 
# Did this code successfully run on Leetcode : 
# Any problem you faced while coding this : 
#
#
# Your code here along with comments explaining your approach
# 1.
# 2. 
# 3.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if word1 is None:
            return len(word2)
        
        elif word2 is None:
            return len(word1)
        
        dp = [[None for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        
        for r in range(0, len(dp)):
            dp[r][0] = r
            
        for c in range(1, len(dp[0])):
            dp[0][c] = c
            
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                
                if word1[c - 1] == word2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                    
                else:
                    dp[r][c] = min(dp[r][c - 1], dp[r - 1][c - 1], dp[r - 1][c]) + 1
                    
        return dp[-1][-1]
