#include <iostream>
#include "linkedLists.h"

using namespace std;

int main(int argc, char **argv){

    SinglyLinkedList sll = SinglyLinkedList();
    sll.pushHead(1);
    sll.pushHead(2);
    float val = sll.popHead();
    cout << val << endl;
}