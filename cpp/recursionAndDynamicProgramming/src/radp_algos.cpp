#include "radp_algos.h"

int Fibonacci::tabulationMethod(int n){
    if(n == 0 or n == 1){
        return n;
    }
    
    std::map<int,int> map = {};
    map[0] = 0;
    map[1] = 1;
    for(int i = 2; i <= n; i++){
        map[i] = map[i-1] + map[i-2];
    }

    return map[n];
}

int Fibonacci::memoizationMethod(int n){
    std::map<int,int> map = {};
    return memoizationMethod(n, map);
}

int Fibonacci::memoizationMethod(int n, std::map<int,int>& map){
    if(n == 0 or n == 1){
        return n;
    }
    if(map.count(n) == 0){
        map[n] = memoizationMethod(n-1, map) + memoizationMethod(n-2, map);
    }
    return map[n];
}

