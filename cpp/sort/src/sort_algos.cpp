#include "sort_algos.h"

typedef std::vector<int> vec;

vec BubbleSort::sort(vec list_to_sort){
    vec x = list_to_sort;
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

vec QuickSort::sort(vec list_to_sort){
    vec x = list_to_sort;
    int list_length = x.size();
    if(list_length==0 or list_length==1){
        return x;
    }
    int high = list_length - 1;
    int low = 0;
    swap_around_pivot(x, high, low);

return x;
}

void QuickSort::swap_around_pivot(vec& z, int high, int low){

    if(high <= low){
        return;
    }

    int pivot = z[high];
    int i = low;
    for(int j = low; j < high; j++){
        if(z[j] <= pivot){
            std::swap(z[i], z[j]);
            i++;
        }
    }
    std::swap(z[i], z[high]);

    swap_around_pivot(z, i-1, low);
    swap_around_pivot(z, high, i);
}