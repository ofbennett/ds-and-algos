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

TowersOfHanoi::TowersOfHanoi(int n): n(n){
    origin = std::list<int>{};
    buffer = std::list<int>{};
    destination = std::list<int>{};
    for (int i = 0; i < n; i++){
        origin.push_front(i);
    }
}

// Set verbose = True in order to print the solution move sequence to screen
void TowersOfHanoi::solve(bool verbose){
    if(verbose) {
        std::cout << "Game begins in current state:" << std::endl;
        printTowerStates();
        std::cout << "Sequence of moves to solve:" << std::endl;
        std::cout << "*********************" << std::endl;
    }
    moveDisks(n, this->origin, this->destination, this->buffer, verbose);
}

void TowersOfHanoi::moveDisks(int n, std::list<int>& origin_c, std::list<int>& destination_c, std::list<int>& buffer_c, bool verbose){
    if(n<=0){
        return;
    }
    else if(n==1){
        // Rule check: ensure disk is being placed on top of larger disk
        if(origin_c.back() >= destination_c.back() and destination_c.size() > 0){
            throw "Disk rule broken.";
        }
        destination_c.push_back(origin_c.back());
        origin_c.pop_back();
        if(verbose){
            printTowerStates();
        }
    }
    else{
        moveDisks(n-1, origin_c, buffer_c, destination_c, verbose);
        moveDisks(1, origin_c, destination_c, buffer_c, verbose);
        moveDisks(n-1, buffer_c, destination_c, origin_c, verbose);
    }
}

void TowersOfHanoi::printTowerStates(){
    std::cout << "origin:      [ ";
    printList(this->origin);
    std::cout << "]" << std::endl;
    std::cout << "buffer:      [ ";
    printList(this->buffer);
    std::cout << "]" << std::endl;
    std::cout << "destination: [ ";
    printList(this->destination);
    std::cout << "]" << std::endl;
    std::cout << "*********************" << std::endl;
}

void TowersOfHanoi::printList(std::list<int>& list){
    for(std::list<int>::iterator it=list.begin(); it != list.end(); ++it){
        std::cout << *it << " ";
    }
}
