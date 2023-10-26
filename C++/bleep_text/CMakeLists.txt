cmake_minimum_required(VERSION 3.26)
project(bleep_text)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(bleep_text
        bleep.cpp
        functions.cpp
        functions.h)
