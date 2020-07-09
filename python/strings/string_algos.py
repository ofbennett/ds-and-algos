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