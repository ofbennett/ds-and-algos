#include "linkedLists.h"

SinglyLinkedList::Node::Node(){
    next = nullptr;
    value = nullptr;
}

SinglyLinkedList::Node::Node(float init_value){
    next = nullptr;
    value = new float(init_value);
}

SinglyLinkedList::Node::~Node(){
    delete value;
}

SinglyLinkedList::SinglyLinkedList(){
    head = nullptr;
}

SinglyLinkedList::SinglyLinkedList(std::vector<float> vec){
    head = nullptr;
    std::reverse(vec.begin(), vec.end());
    for(int i = 0; i < vec.size(); i++){
        this->pushHead(vec[i]);
    }
}

SinglyLinkedList::~SinglyLinkedList(){
    Node* current = head;
    while (current != nullptr){
        Node* prev_node  = current;
        current = current->next;
        delete prev_node;
    }
}

void SinglyLinkedList::pushHead(float value){
    Node* node = new Node(value);
    if (head == nullptr){
        head = node;
    } else {
        node->next = head;
        head = node;
    }
}

float SinglyLinkedList::popHead(){
    if (head == nullptr){
        std::cerr << "popHead: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    }
    Node* old_head = head;
    if (head->next == nullptr) {
        head = nullptr;
    } else {
        head = head->next;
    }

    float value = *(old_head->value);
    delete old_head;

    return value;
}

float SinglyLinkedList::getHead(){
    if (head == nullptr){
        std::cerr << "getHead: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    } else {
        float value = *(head->value);
        return value;
    }
}

float SinglyLinkedList::getTail(){
    if (head == nullptr){
        std::cerr << "getTail: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    } else {
        Node* tail = this->getTailNode();
        float value = *(tail->value);
        return value;
    }
}

int SinglyLinkedList::getLength(){
    Node* current = head;
    int n = 0;
    while (current != nullptr){
        current = current->next;
        n++;
    }
    return n;
}

void SinglyLinkedList::pushTail(float value){
    Node* node = new Node(value);
    if (head == nullptr){
        head = node;
    } else {
        Node* tail = this->getTailNode();
        tail->next = node;
    }
}

float SinglyLinkedList::popTail(){
    if (head == nullptr){
        std::cerr << "popTail: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    } else if (head->next == nullptr) {
        float value = *(head->value);
        delete(head);
        head = nullptr;
        return value;
    } else {
        Node* current = head;
        Node* prev = nullptr;
        while (current->next != nullptr){
            prev = current;
            current = current->next;
        }
        prev->next = nullptr;
        float value = *(current->value);
        delete current;
        return value;
    }
}

SinglyLinkedList::Node* SinglyLinkedList::getTailNode(){
    Node* current = head;
    while (current->next != nullptr){
        current = current->next;
    }
    return current;
}

std::vector<float> SinglyLinkedList::getVector(){
    std::vector<float> vec;
    if (head == nullptr){
        return vec;
    } else {
        Node* current = head;
        while (current->next != nullptr) {
            vec.push_back(*(current->value));
            current = current->next;
        }
        vec.push_back(*(current->value));
        return vec;
    }
}

float SinglyLinkedList::valueAt(int index){
    int length = this->boundCheck(index);
    Node* current = head;
    for(int i = 0; i < index; i++){
        current = current->next;
    }
    float value = *(current->value);
    return value;
}

void SinglyLinkedList::deleteAt(int index){
    int length = this->boundCheck(index);
    if (index == 0){
        Node* new_head = head->next;
        delete head;
        head = new_head;
    } else {
        Node* current = head;
        for(int i = 0; i < index-1; i++){
            current = current->next;
        }
        Node* node_to_delete = current->next;
        if (node_to_delete->next != nullptr){
            Node* node_after_deletion = node_to_delete->next;
            current->next = node_after_deletion;
        } else {
            current->next = nullptr;
        }
        delete node_to_delete;
    }
}

void SinglyLinkedList::insertAt(int index, float value){
    int length = this->boundCheck(index);
    Node* new_node = new Node(value);
    if (index == 0){
        new_node->next = head;
        head = new_node;
    } else {
        Node* current = head;
        for(int i = 0; i < index-1; i++){
            current = current->next;
        }
        Node* node_after = current->next;
        current->next = new_node;
        new_node->next = node_after;
    }
}

int SinglyLinkedList::boundCheck(int index){
    int length = this->getLength();
    if (index > length - 1 or index < 0) {
        std::cerr << "boundCheck: Index " << index << " out of range for list of length " << length << std::endl;
        exit(EXIT_FAILURE);
    }
    return length;
}

void SinglyLinkedList::reverse(){
    int length = this->getLength();
    if (length == 0 or length == 1){
        return;
    }
    Node* node1 = head;
    Node* node2 = head->next;
    head->next = nullptr;
    Node* node3;
    while(node2->next != nullptr){
        node3 = node2->next;
        node2->next = node1;
        node1 = node2;
        node2 = node3;
    }
    node2->next = node1;
    head = node2;
}

////////////////////////////////////////////////////////////////

DoublyLinkedList::Node::Node(){
    next = nullptr;
    prev = nullptr;
    value = nullptr;
}

DoublyLinkedList::Node::Node(float init_value){
    next = nullptr;
    prev = nullptr;
    value = new float(init_value);
}

DoublyLinkedList::Node::~Node(){
    delete value;
}

DoublyLinkedList::DoublyLinkedList(){
    head = nullptr;
    tail = nullptr;
}

DoublyLinkedList::DoublyLinkedList(std::vector<float> vec){
    head = nullptr;
    tail = nullptr;
    std::reverse(vec.begin(), vec.end());
    for(int i = 0; i < vec.size(); i++){
        this->pushHead(vec[i]);
    }
}

DoublyLinkedList::~DoublyLinkedList(){
    Node* current = head;
    while (current != nullptr){
        Node* prev_node  = current;
        current = current->next;
        delete prev_node;
    }
}

void DoublyLinkedList::pushHead(float value){
    Node* node = new Node(value);
    if (head == nullptr){
        head = node;
        tail = node;
    } else {
        node->next = head;
        head->prev = node;
        head = node;
    }
}

float DoublyLinkedList::popHead(){
    if (head == nullptr){
        std::cerr << "popHead: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    }
    Node* old_head = head;
    if (head->next == nullptr) {
        head = nullptr;
        tail = nullptr;
    } else {
        head = head->next;
        head->prev = nullptr;
    }

    float value = *(old_head->value);
    delete old_head;

    return value;
}

float DoublyLinkedList::getHead(){
    if (head == nullptr){
        std::cerr << "getHead: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    } else {
        float value = *(head->value);
        return value;
    }
}

float DoublyLinkedList::getTail(){
    if (tail == nullptr){
        std::cerr << "getTail: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    } else {
        float value = *(tail->value);
        return value;
    }
}

int DoublyLinkedList::getLength(){
    Node* current = head;
    int n = 0;
    while (current != nullptr){
        current = current->next;
        n++;
    }
    return n;
}

void DoublyLinkedList::pushTail(float value){
    Node* node = new Node(value);
    if (tail == nullptr){
        head = node;
        tail = node;
    } else {
        tail->next = node;
        node->prev = tail;
        tail = node;
    }
}

// Debugging method used to ensure all necessary links between Nodes exist
bool DoublyLinkedList::is_connected(){
    if(head == nullptr){
        return true;
    }
    Node* current = head;
    while(current->next != nullptr){
        current = current->next;
    }
    if(current != tail){
        return false;
    }
    while(current->prev != nullptr){
        current = current->prev;
    }
    if(current != head){
        return false;
    }
    return true;
}

float DoublyLinkedList::popTail(){
    if (tail == nullptr){
        std::cerr << "popTail: List is empty" << std::endl;
        exit(EXIT_FAILURE);
    }
    float value = *(tail->value);
    if (tail->prev == nullptr) {
        delete(tail);
        tail = nullptr;
        head = nullptr;
    } else {
        Node* old_tail = tail;
        tail = tail->prev;
        tail->next = nullptr;
        delete(old_tail);
    }
    return value;
}

std::vector<float> DoublyLinkedList::getVector(){
    std::vector<float> vec;
    if (head == nullptr){
        return vec;
    } else {
        Node* current = head;
        while (current->next != nullptr) {
            vec.push_back(*(current->value));
            current = current->next;
        }
        vec.push_back(*(current->value));
        return vec;
    }
}

float DoublyLinkedList::valueAt(int index){
    int length = this->boundCheck(index);
    Node* current = head;
    for(int i = 0; i < index; i++){
        current = current->next;
    }
    float value = *(current->value);
    return value;
}

int DoublyLinkedList::boundCheck(int index){
    int length = this->getLength();
    if (index > length - 1 or index < 0) {
        std::cerr << "boundCheck: Index " << index << " out of range for list of length " << length << std::endl;
        exit(EXIT_FAILURE);
    }
    return length;
}

void DoublyLinkedList::deleteAt(int index){
    int length = this->boundCheck(index);
    if ((index == 0) and (head != tail)){
        Node* new_head = head->next;
        delete head;
        head = new_head;
        head->prev = nullptr;
    } else if ((index == 0) and (head == tail)) {
        delete head;
        head = nullptr;
        tail = nullptr;
    } else if ((index == length - 1) and (head != tail)) {
        Node* new_tail = tail->prev;
        delete tail;
        new_tail->next = nullptr;
        tail = new_tail;
    } else {
        Node* current = head;
        for(int i = 0; i < index-1; i++){
            current = current->next;
        }
        Node* node_to_delete = current->next;
        Node* node_after_deletion = node_to_delete->next;
        current->next = node_after_deletion;
        node_after_deletion->prev = current;
        delete node_to_delete;
    }
}

void DoublyLinkedList::insertAt(int index, float value){
    int length = this->boundCheck(index);
    Node* new_node = new Node(value);
    if (index == 0){
        new_node->next = head;
        head->prev = new_node;
        head = new_node;
    } else {
        Node* current = head;
        for(int i = 0; i < index-1; i++){
            current = current->next;
        }
        Node* node_after = current->next;
        current->next = new_node;
        new_node->next = node_after;
        new_node->prev = current;
        if (node_after != nullptr){
            node_after->prev = new_node;
        }
    } 
}

void DoublyLinkedList::reverse(){
    int length = this->getLength();
    if (length == 0 or length == 1){
        return;
    }
    Node* node1 = head;
    Node* node2 = head->next;
    head->next = nullptr;
    head->prev = node2;
    tail = node1;
    Node* node3;
    while(node2->next != nullptr){
        node3 = node2->next;
        node2->next = node1;
        node2->prev = node3;
        node1 = node2;
        node2 = node3;
    }
    node2->next = node1;
    node2->prev = nullptr;
    head = node2;
}