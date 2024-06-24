# CMakeList.txt : fichier projet CMake de niveau supérieur, effectuez une configuration globale
# et incluez les sous-projets ici.
#
cmake_minimum_required (VERSION 3.8)

project (HelloProject)

set(OSBitness 32)
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
	set(OSBitness 64)
endif()

set(FullOutputDir "${CMAKE_SOURCE_DIR}/../bin/${CMAKE_SYSTEM_NAME} ${OSBitness}/${CMAKE_BUILD_TYPE}")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${FullOutputDir}/Static Library")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${FullOutputDir}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${FullOutputDir}/Dynamic Library")


add_subdirectory ("HelloDll")

# Incluez les sous-projets.
add_subdirectory ("Hello")
