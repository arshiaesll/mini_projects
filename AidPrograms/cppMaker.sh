#!/bin/bash

if [ -z $1 ]; then
  exit 1
fi

mkdir $1 
touch $1/$1.cc
touch $1/makefile
echo "flags= -std=c++17 -Wall -I ." >> $1/makefile
echo "target: $1.cc" >> $1/makefile
echo -e "\tg++ "\$\(flags\) $1.cc"" >> $1/makefile
echo -e "\t./a.out" >>$1/makefile

