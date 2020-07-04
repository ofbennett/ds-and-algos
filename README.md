# My Data Structures and Algorithms

By Oscar Bennett

My own implementation of important and interesting data structures and algorithms written in both Python and C++. Tested with the [pytest](https://docs.pytest.org/en/latest/) and [Catch](https://github.com/catchorg/Catch2) frameworks respectively.

I'm planning to keep this project ongoing and gradually add things over time. Happy to hear suggestions!

## Python Code Done and To Do:

:white_check_mark: == Done

Data Structures:

- Singly Linked List :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/linkedLists/linkedLists.py#L1)
- Doubly Linked List :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/linkedLists/linkedLists.py#L154)
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Bubble Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L3)
- Quick Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L19)
- Merge Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L45)
- Binary Search (of sorted array) :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/search/search_algos.py#L2)
- Tree traversal DFS - Pre Order, In Order, Post Order
- Tree traversal BFS - Level Order
- Graph BFS
- Graph DFS
- Dijkstra
- String Search and Manipulation

## Run Python Code Tests:

```
$ pip install pytest
$ pytest
```

## C++ Code Done and To Do:

:white_check_mark: == Done

Data Structures:

- Singly Linked List :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/linkedLists/src/linkedLists.h#L7)
- Doubly Linked List :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/linkedLists/src/linkedLists.h#L41)
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Bubble Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L5)
- Quick Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L29)
- Merge Sort :white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L62)
- Binary Search (of sorted array)
- Tree traversal DFS - Pre Order, In Order, Post Order
- Tree traversal BFS - Level Order
- Graph BFS
- Graph DFS
- Dijkstra
- String Search and Manipulation

## To Build and Run C++ Code:
Requires an installation of [cmake](https://cmake.org).

```
$ cd cpp/build
$ ccmake ..
```
- Hit C, Hit C, Hit G. This should configure and generate a make file.
```
$ make
```
All binaries will be built and placed in the `build/bin` directory. To run one of the binaries for example run:
```
$ bin/test_singlyLinkedLists
```