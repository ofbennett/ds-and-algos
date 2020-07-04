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
    void swap_around_pivot(vec& z, int high, int low);
};

class MergeSort {
    public:
    vec sort(vec list_to_sort);
    private:
    void _sort(vec& z);
    void _merge(vec& z, vec& L, vec& R);
};

// Debugging function for printing out vectors
void PrintVec(vec v);

#endif /* SORT_ALGOS_H_ */