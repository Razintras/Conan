@echo off
mkdir build
cd build || exit /b
::cmake ../src/ -G "Visual Studio 15 2017"
cmake ../src/
cmake --build .