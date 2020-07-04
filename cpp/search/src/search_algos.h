#ifndef SEARCH_ALGOS_H_
#define SEARCH_ALGOS_H_

#include <vector>
#include <iostream>

typedef std::vector<int> vec;

class BinarySearch{
    public:
    bool recursive_search(const vec& sorted_list, const int item);
    bool iterative_search(const vec& sorted_list, const int item);
    private:
    bool search_range(const vec& sorted_list, int high, int low, const int item);
};

class SequentialSearch{
    public:
    bool search(const vec& sorted_list, const int item);
};

#endif /* SEARCH_ALGOS_H_ */