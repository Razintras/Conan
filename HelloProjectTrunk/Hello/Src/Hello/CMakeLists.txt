# CMakeList.txt : projet CMake pour Hello, incluez la source et définissez
# la logique spécifique au projet ici.
#
cmake_minimum_required (VERSION 3.8)
project (hello)

include_directories( ${CMAKE_CURRENT_SOURCE_DIR}/../HelloDll/ )
link_directories( ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY} )

add_executable (Hello "Hello.cpp" )

target_link_libraries( Hello hellodll )


