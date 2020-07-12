from collections import deque

class Fibonacci:
    # Dynamic programming methods for O(N) calculation of the Nth Fibonacci number. Recursive algorithm is ~O(1.6^N).
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

class TowersOfHanoi:
    # Recursive algorithm which solves the Towers of Hanoi puzzle. Time complexity O(2^N) where N is number of disks.
    def __init__(self, n):
        self.n = n
        self.origin = deque()
        self.buffer = deque()
        self.destination = deque()
        for i in reversed(range(n)):
            self.origin.append(i)
    
    # Set verbose = True in order to print the solution move sequence to screen
    def solve(self, verbose=False):
        if verbose:
            print("Game begins in current state:")
            self.printTowerStates()
            print("Sequence of moves to solve:")
            print("******************")
        self.moveDisks(self.n, self.origin, self.destination, self.buffer, verbose)
    
    def moveDisks(self, n, origin, destination, buffer, verbose=False):
        if n <= 0:
            return
        elif n == 1:
            if len(destination) > 0:
                assert(origin[-1] < destination[-1]) # Rule check: ensure disk is being placed on top of larger disk
            destination.append(origin.pop())
            if verbose:
                self.printTowerStates()
        else:
            self.moveDisks(n-1, origin, buffer, destination, verbose)
            self.moveDisks(1, origin, destination, buffer, verbose)
            self.moveDisks(n-1, buffer, destination, origin, verbose)
    
    def printTowerStates(self):
        print("origin:      ", list(self.origin))
        print("buffer:      ", list(self.buffer))
        print("destination: ", list(self.destination))
        print("******************")