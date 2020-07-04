#ifndef SORT_ALGOS_H_
#define SORT_ALGOS_H_

#include <vector>
#include <iostream>

typedef std::vector<int> vec;

class BubbleSort {
    public:
    vec sort(vec list_to_sort);
};

class QuickSort {
    public:
    vec sort(vec list_to_sort);
    private:
    void swap_around_pivot(vec z, int high, int low);
};


#endif /* SORT_ALGOS_H_ */