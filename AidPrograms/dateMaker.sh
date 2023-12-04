#!/bin/bash


Date=$(date "+%V")
if ! [ -e "$Date.txt" ]; then
  cat ~/selfstudy/Utils/resources/dateTemple.txt >> "$Date.txt"
  # vim ~/Save/ToDo/"$Date.txt"
fi

vim ~/Save/ToDo/$(ls ~/Save/ToDo/ -t | head -1)

