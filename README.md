# Data Structures and Algorithms

By Oscar Bennett

My own implementation of important data structures and algorithms written in both Python and C++. Tested with the [pytest](https://docs.pytest.org/en/latest/) and [Catch](https://github.com/catchorg/Catch2) frameworks respectively.

## Python Code Done and To Do:

Data Structures:

- Singly Linked List :white_check_mark:
- Doubly Linked List :white_check_mark:
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Binary Search
- Bubble Sort
- Merge Sort
- Quick Sort
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

Data Structures:

- Singly Linked List :white_check_mark:
- Doubly Linked List :white_check_mark:
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Binary Search
- Bubble Sort
- Merge Sort
- Quick Sort
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
- Hit C, Hit C, Hit G. This should generate a make file.
```
$ make
```
All binaries will be built and placed in the `build/bin` directory. To run one of the binaries for example run:
```
$ bin/test_singlyLinkedLists
```