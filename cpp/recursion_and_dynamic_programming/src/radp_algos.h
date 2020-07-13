#ifndef RADP_ALGOS_H_
#define RADP_ALGOS_H_

#include <iostream>
#include <map>
#include <list>

class Fibonacci{
    public:
    int tabulationMethod(int n);
    int memoizationMethod(int n);
    private:
    int memoizationMethod(int n, std::map<int,int>& map);
};

class TowersOfHanoi{
    public:
    TowersOfHanoi(int n);
    void solve(bool verbose=false);
    int n;
    std::list<int> origin;
    std::list<int> buffer;
    std::list<int> destination;
    
    private:
    void moveDisks(int n, std::list<int>& origin, std::list<int>& destination, std::list<int>& buffer, bool verbose);
    void printTowerStates();
    void printList(std::list<int>& list);
};

#endif /* RADP_ALGOS_H_ */