cmake_minimum_required(VERSION 3.8)
project(Lesson3_Prediction_C__)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        classifier.cpp
        classifier.h
        main.cpp)

add_executable(Lesson3_Prediction_C__ ${SOURCE_FILES})