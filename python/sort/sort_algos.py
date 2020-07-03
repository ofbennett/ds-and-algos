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