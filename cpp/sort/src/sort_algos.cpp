#include "sort_algos.h"

typedef std::vector<int> vec;

vec BubbleSort::sort(vec list_to_sort){
    vec x = vec(list_to_sort); // copy list_to_sort
    if(x.size()==0 or x.size()==1){
        return x;
    }
    while(true){
        int swap_count = 0;
        int temp;
        for(int i = 0; i < x.size()-1; i++){
            if(x[i] > x[i+1]){
                swap_count++;
                // Swap values:
                temp = x[i];
                x[i] = x[i+1];
                x[i+1] = temp;
            }
        }
        if(swap_count == 0){
            break;
        }
    }
    return x;
}