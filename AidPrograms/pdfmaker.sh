#!/bin/bash



P=$(ls -t ~/Downloads | head -1)
# echo ~/Downloads/$P.pptx

echo $P
# cat ~/Downloads/"$P"
# We assume the file is going to be .pptx (always)
Name=${P::-5}

echo $Name
soffice --convert-to pdf ~/Downloads/"$P"
mv "$Name".pdf ~/School/notes


