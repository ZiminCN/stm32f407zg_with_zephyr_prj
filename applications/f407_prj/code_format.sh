#!bin/bash
clang-format -i Bsp/include/*.hpp
clang-format -i Bsp/include/*.h
clang-format -i Bsp/src/*.cpp
clang-format -i Bsp/src/*.c
clang-format -i Core/include/*.hpp
clang-format -i Core/include/*.h
clang-format -i Core/src/*.cpp
clang-format -i Core/src/*.c
rm -rf .vscode/
