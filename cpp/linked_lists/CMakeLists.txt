include_directories(src)
add_subdirectory(src)
add_subdirectory(tests)

add_executable(linkedListsExamples linkedLists_examples.cpp)
target_link_libraries(linkedListsExamples linkedLists_library)