
class BinarySearch:
    def __init__(self):
        pass

    def recursive_search(self, sorted_list, item):
        """
        Searches to find if item is in the sorted list.
        Method calls _search_range() recursively.
        """
        low = 0
        high = len(sorted_list) - 1
        answer = self._search_range(sorted_list, high, low, item)
        return answer


    def _search_range(self, sorted_list, high, low, item):
        if low > high:
            return False
        mid = (high - low)//2 + low
        if item > sorted_list[mid]:
            low = mid + 1
        if item < sorted_list[mid]:
            high = mid - 1
        if item == sorted_list[mid]:
            return True
        return self._search_range(sorted_list, high, low, item)

    def iterative_search(self, sorted_list, item):
        """
        Searches to find if item is in the sorted list.
        Method runs iteratively.
        """
        high = len(sorted_list)-1
        low = 0
        while(True):
            if low > high:
                return False
            mid = (high-low)//2 + low
            if item > sorted_list[mid]:
                low = mid+1
            if item < sorted_list[mid]:
                high = mid-1
            if item == sorted_list[mid]:
                return True

# Naive SequentialSearch implemented for benchmark comparisons
class SequentialSearch:
    def __init__(self):
        pass

    def search(self, sorted_list, item):
        for i in sorted_list:
            if i == item:
                return True
        return False
