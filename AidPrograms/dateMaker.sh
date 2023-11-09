#!/bin/bash


Date=$(date "+%V")
if [ -e "$Date.txt" ]; then
  vim "$Date.txt"
else
  cat ~/selfstudy/Utils/resources/dateTemple.txt >> "$Date.txt"
  vim "$Date.txt"
fi

