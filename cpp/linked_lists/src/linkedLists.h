#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include <vector>
#include <iostream>

class SinglyLinkedList {
    class Node {
        public:
        Node* next;
        float* value;
        Node();
        Node(float value);
        ~Node();
    };

    public:
    SinglyLinkedList();
    SinglyLinkedList(std::vector<float> vec);
    ~SinglyLinkedList();

    void pushHead(float value);
    float popHead();
    float getHead() const;
    float getTail() const;
    int getLength() const;
    void pushTail(float value);
    float popTail();
    std::vector<float> getVector() const;
    float valueAt(int index) const;
    void deleteAt(int index);
    void insertAt(int index, float value);
    void reverse();

    private:
    Node* getTailNode() const;
    int boundCheck(int index) const;
    Node* head;
};

class DoublyLinkedList {
    class Node {
        public:
        Node* next;
        Node* prev;
        float* value;
        Node();
        Node(float value);
        ~Node();
    };

    public:
    DoublyLinkedList();
    DoublyLinkedList(std::vector<float> vec);
    ~DoublyLinkedList();

    void pushHead(float value);
    float popHead();
    float getHead() const;
    float getTail() const;
    int getLength() const;
    void pushTail(float value);
    float popTail();
    std::vector<float> getVector() const;
    float valueAt(int index) const;
    void deleteAt(int index);
    void insertAt(int index, float value);
    void reverse();
    bool is_connected() const;

    private:
    Node* getTailNode() const;
    int boundCheck(int index) const;
    Node* head;
    Node* tail;
};

#endif /* LINKEDLIST_H_ */