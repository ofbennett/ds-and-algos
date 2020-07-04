#include "search_algos.h"

typedef std::vector<int> vec;

bool BinarySearch::recursive_search(const vec& sorted_list, const int item){

    int low = 0;
    int high = sorted_list.size() - 1;
    bool answer = search_range(sorted_list, high, low, item);
    return answer;
}

bool BinarySearch::iterative_search(const vec& sorted_list, const int item){

    int low = 0;
    int high = sorted_list.size() - 1;
    while(true){
        if(low > high){
            return false;
        }
        int mid = (high - low)/2 + low;
        if(item > sorted_list[mid]){
            low = mid + 1;
        }
        if(item < sorted_list[mid]){
            high = mid - 1;
        }
        if(item == sorted_list[mid]){
            return true;
        }
    }
}

bool BinarySearch::search_range(const vec& sorted_list, int high, int low, const int item){

    if(low > high){
        return false;
    }
    int mid = (high - low)/2 + low;
    if(item > sorted_list[mid]){
        low = mid + 1;
    }
    if(item < sorted_list[mid]){
        high = mid - 1;
    }
    if(item == sorted_list[mid]){
        return true;
    }
    return search_range(sorted_list, high, low, item);
}

bool SequentialSearch::search(const vec& sorted_list, const int item){

    for (int i = 0; i < sorted_list.size(); i++){
        if(sorted_list[i] == item){
            return true;
        }
    }
    return false;
}