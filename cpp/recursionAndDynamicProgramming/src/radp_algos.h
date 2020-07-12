#ifndef RADP_ALGOS_H_
#define RADP_ALGOS_H_

#include <iostream>
#include <map>

class Fibonacci{
    public:
    int tabulationMethod(int n);
    int memoizationMethod(int n);
    private:
    int memoizationMethod(int n, std::map<int,int>& map);
};

#endif /* RADP_ALGOS_H_ */