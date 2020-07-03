from copy import copy
class BubbleSort:
    def __init__(self):
        pass

    def sort(self, list_to_sort):
        x = copy(list_to_sort)
        while(True):
            swap_count = 0
            for i in range(len(x)-1):
                if(x[i] > x[i+1]):
                    swap_count += 1
                    x[i], x[i+1] = x[i+1], x[i]
            if swap_count == 0:
                break
        return x

class QuickSort:
    def __init__(self):
        pass

    def sort(self, list_to_sort):
        x = copy(list_to_sort)
        low = 0
        high = len(x) - 1
        self._swap_around_pivot(x, high, low)
        return x

    def _swap_around_pivot(self, z, high, low):
        if high <= low:
            return

        pivot = z[high]
        i = low
        for j in range(low, high):
            if z[j] <= pivot:
                z[i], z[j] = z[j], z[i]
                i +=1
        z[i], z[high] = z[high], z[i]

        self._swap_around_pivot(z, i-1, low)
        self._swap_around_pivot(z, high, i)

class MergeSort:
    def __init__(self):
        pass

    def sort(self, list_to_sort):
        x = copy(list_to_sort)
        self._sort(x)
        return x

    def _sort(self, z):
        if len(z) >1:
            m = len(z)//2
            L = z[:m]
            R = z[m:]
            self._sort(L)
            self._sort(R)
            self._merge(z, L, R)

    def _merge(self, z, L, R):
        # Merge L and R arrays assuming they are both individually sorted 
        i = j = k = 0
        while (i<len(L)) and (j<len(R)):
            if L[i] < R[j]:
                z[k] = L[i]
                i +=1
                k +=1
            else:
                z[k] = R[j]
                j +=1
                k +=1
        while (i<len(L)):
            z[k] = L[i]
            i +=1
            k +=1
        while (j<len(R)):
            z[k] = R[j]
            j +=1
            k +=1