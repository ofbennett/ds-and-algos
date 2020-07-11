class SubstringSearch:
    def __init__(self):
        pass

    def longestNoneRepeatingChars(self, string):
        # Sliding window approach. Should be ~O(N)
        start = 0
        end = 0
        startLongest = 0
        endLongest = 0
        currentLongest = 0
        charSet = set()
        charIndices = dict()
        while(end < len(string)):
            if string[end] in charSet:
                repeatedCharIndex = charIndices[string[end]]
                while(start != repeatedCharIndex + 1):
                    charSet.remove(string[start])
                    charIndices[string[start]] = None
                    start += 1
            charSet.add(string[end])
            charIndices[string[end]] = end
            end += 1
            currentLength = end - start
            if currentLength > currentLongest:
                currentLongest = currentLength
                startLongest = start
                endLongest = end
                currentLongest = endLongest - startLongest
        return string[startLongest:endLongest]
    
    def rabinKarp(self, string, substring):
        rfpsw = self.RabinFingerPrintSlidingWindow(string, len(substring))
        ssHash = rfpsw.rabinFingerPrint(substring)
        candidateHash = rfpsw.firstHash()
        while(candidateHash is not None):
            if ssHash == candidateHash:
                candidateSubstring = string[rfpsw.start:rfpsw.end]
                if substring == candidateSubstring:
                    return True
            candidateHash = rfpsw.nextHash()
        return False

    class RabinFingerPrintSlidingWindow:
        def __init__(self, string, hashLength):
            self.string = string
            self.hashLength = hashLength
            self.currentHash = -1
            self.a = 128 # polynomial coefficient 
            self.q = 4096 # modulo constant
            self.start = 0
            self.end = hashLength
        
        def firstHash(self):
            result = self.rabinFingerPrint(self.string[:self.hashLength])
            self.currentHash = result
            return result

        def nextHash(self):
            # Shift window right by one
            if self.end >= len(self.string):
                return None
            result = (((self.currentHash - (ord(self.string[self.start]) * (self.a ** (self.hashLength - 1)))) * self.a) + ord(self.string[self.end])) % self.q
            self.currentHash = result
            self.start += 1
            self.end += 1
            return result

        def rabinFingerPrint(self, substring):
            n = 0
            total = 0
            for char in reversed(substring):
                total += (ord(char) * (self.a ** n)) % self.q
                n += 1
            return total