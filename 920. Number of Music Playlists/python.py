class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        self.n = n
        self.k = k
        # dp[i][j] := # of playlists with i songs and j different songs
        self.dp = [[-1 for _ in range(n + 1)] for _ in range(goal + 1)]
        return self.playlists(goal, n)

    kMod = 1000000007

    def playlists(self, i: int, j: int) -> int:
        if i == 0:
            return int(j == 0)
        if j == 0:
            return 0
        if self.dp[i][j] >= 0:
            return self.dp[i][j]

        self.dp[i][j] = self.playlists(i - 1, j - 1) * (self.n - (j - 1))  # Last song is new
        self.dp[i][j] += self.playlists(i - 1, j) * max(0, j - self.k)     # Last song is old
        return self.dp[i][j] % self.kMod
