#!/bin/bash


P=$(ls -t ~/Pictures/Screenshots/ | head -1)

cp ~/Pictures/Screenshots/"$P" .

