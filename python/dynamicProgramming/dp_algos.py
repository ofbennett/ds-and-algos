class Fibonacci:
    def __init__(self):
        pass

    def tabulationMethod(self, n):
        # Bottom up
        if n in [0,1]:
            return n
        
        memo = {}
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

    def memoizationMethod(self, n):
        # Top down
        memo = {}
        return self._memoizationMethod(n, memo)

    def _memoizationMethod(self, n, memo):
        if n in [0,1]:
            return n
        
        if n not in memo.keys():
            memo[n] = self._memoizationMethod(n-1, memo) + self._memoizationMethod(n-2, memo)
        
        return memo[n]