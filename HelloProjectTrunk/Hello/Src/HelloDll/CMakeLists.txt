# CMakeList.txt : projet CMake pour Hello, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)
project (hellodll)

add_library (hellodll SHARED "hellodll.cpp")


