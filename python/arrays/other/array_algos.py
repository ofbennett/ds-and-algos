from copy import copy

class Rotate:
    def __init__(self):
        pass

    def rotate_extra_array(self, list_to_rotate, k):
        """
        Builds rotated array within a temporary new array in memory. Time O(N), Space O(N).
        """
        
        x1 = copy(list_to_rotate)
        length = len(x1)
        if length == 0:
            return x1
        k = k % length
        if k == 0:
            return x1
        x2 = copy(list_to_rotate)
        for i in range(length):
            x2[(i+k) % length] = x1[i]

        x1 = x2
        return x1
    
    def rotate_cycles(self, list_to_rotate, k):
        """
        Swaps elements of array in place in a single pass. Time O(N), Space O(1).
        """
        x = copy(list_to_rotate)
        length = len(x)
        if length == 0:
            return x
        k = k % length
        if k == 0:
            return x

        start = 0
        count = 0
        while count < length:
            current_ind = start
            next_ind = (start + k) % length
            next_value = x[start]
            while True:
                current_ind = next_ind
                next_ind = (current_ind + k) % length
                temp = x[current_ind]
                x[current_ind] = next_value
                next_value = temp
                count += 1
                if current_ind == start:
                    break
            start += 1
        return x
