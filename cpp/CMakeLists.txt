cmake_minimum_required(VERSION 3.5)
project(ds_algos)

add_definitions(-std=c++11)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

include_directories(catch)

add_subdirectory(linkedLists)
add_subdirectory(sort)
add_subdirectory(search)
add_subdirectory(graphs)
add_subdirectory(recursionAndDynamicProgramming)