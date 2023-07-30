class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # dp[i][j] := min # of turns to print s[i..j]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        return self.strangePrinterHelper(s, 0, n - 1, dp)

    def strangePrinterHelper(self, s: str, i: int, j: int, dp: List[List[int]]) -> int:
        if i > j:
            return 0
        if dp[i][j] > 0:
            return dp[i][j]

        # Print s[i]
        dp[i][j] = self.strangePrinterHelper(s, i + 1, j, dp) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                dp[i][j] = min(dp[i][j], self.strangePrinterHelper(s, i, k - 1, dp) + self.strangePrinterHelper(s, k + 1, j, dp))

        return dp[i][j]
