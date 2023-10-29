# Temple makefile for cpp


flags= -std=c++17 -Wall -I


a.out : $1.cc 
  g++ $flags $<
  ./a.out

