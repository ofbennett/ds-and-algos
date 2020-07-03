# My Data Structures and Algorithms

By Oscar Bennett

My own implementation of important and interesting data structures and algorithms written in both Python and C++. Tested with the [pytest](https://docs.pytest.org/en/latest/) and [Catch](https://github.com/catchorg/Catch2) frameworks respectively.

I'm planning to keep this project ongoing and gradually add things over time. Happy to hear suggestions!

## Python Code Done and To Do:

:white_check_mark: == Done

Data Structures:

- Singly Linked List :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/fe6322a1c5f0f00b7c2bed23de667185fa66c61d/python/linkedLists/linkedLists.py#L1)
- Doubly Linked List :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/6d8fd4e238803236ccb3ad176204804a098687f9/python/linkedLists/linkedLists.py#L154)
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Bubble Sort :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/python/sort/sort_algos.py#L3)
- Merge Sort :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/python/sort/sort_algos.py#L45)
- Quick Sort :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/python/sort/sort_algos.py#L19)
- Binary Search (of sorted array) :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/python/search/search_algos.py#L2)
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

- Singly Linked List :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/cpp/linkedLists/src/linkedLists.h#L7)
- Doubly Linked List :white_check_mark: - [link](https://github.com/ofbennett/Data_Structures_and_Algorithms/blob/e1fdbf44f47bf36106a31110191cff8f246f513a/cpp/linkedLists/src/linkedLists.h#L41)
- Hash Table
- Tree
- Graph
- Heap
- Trie

Algorithms:

- Bubble Sort
- Merge Sort
- Quick Sort
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