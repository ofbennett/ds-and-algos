# My Data Structures and Algorithms

By Oscar Bennett

These are my own Python and C++ implementations of some important and interesting data structures and algorithms. Tested with the Python [pytest](https://docs.pytest.org/en/latest/) and the C++ [Catch2](https://github.com/catchorg/Catch2) frameworks respectively.

I'm planning to keep this project ongoing and gradually add things over time. Happy to hear suggestions!

## Code Done and To Do:

:white_check_mark: == Done

Data Structures | Python | C++
----------------|--------|----
Singly Linked List|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/linkedLists/linkedLists.py#L1)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/linkedLists/src/linkedLists.h#L7)
Doubly Linked List|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/linkedLists/linkedLists.py#L154)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/linkedLists/src/linkedLists.h#L41)
Hash Table||
Graph (Adjacency List)|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/python/graphs/graph_ds.py#L1)|
Graph (Objects and Pointers)|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/python/graphs/graph_ds.py#L8)|
Binary Tree|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/python/trees/tree_ds.py#L14)|
Heap||
Trie||

Algorithms | Python | C++
-----------|--------|----
Bubble Sort|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L3)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L5)
Quick Sort|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L19)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L29)
Merge Sort|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/sort/sort_algos.py#L45)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/cpp/sort/src/sort_algos.cpp#L62)
Binary Search (of sorted array)|:white_check_mark: - [link](https://github.com/ofbennett/my-ds-and-algos/blob/master/python/search/search_algos.py#L2)|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/cpp/search/src/search_algos.cpp#L5)
Graph DFS|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/python/graphs/graph_algos.py#L25)|
Graph BFS|:white_check_mark: - [link](https://github.com/ofbennett/ds-and-algos/blob/master/python/graphs/graph_algos.py#L72)|
Dijkstra||
Binary Tree Traversal DFS<br>Pre Order, In Order, Post Order<br>Recursive||
Binary Tree Traversal DFS<br>Pre Order, In Order, Post Order<br>Iterative||
String Search||
String Manipulation||

## Run Python Code Tests:

```
$ pip install pytest
$ pytest
```

## Build and Run C++ Code and Tests:
Requires an installation of [cmake](https://cmake.org).

```
$ cd cpp/build
$ ccmake ..
```
- Hit C, Hit C, Hit G. This should configure and generate a make file.
```
$ make
```
All binaries (including all the binaries to run tests) will be built and placed in the `build/bin` directory. To run one of the test binaries for example, run:
```
$ bin/test_singlyLinkedLists
```
The easiest way to run all the C++ tests together is to run the `cpp/run_all_cpp_tests.sh` shell script. To run:
```
$ cd ..
$ bash run_all_cpp_tests.sh
```
