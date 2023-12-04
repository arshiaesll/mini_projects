#!/bin/bash



P=$(ls -t ~/Downloads | head -1)
# echo ~/Downloads/$P.pptx
echo $P
# We assume the file is going to be .pptx (always)
PATH_DOW=~/Downloads/"$P"
if [[ $P == *.pptx ]]; then
  libreoffice --headless --convert-to pdf --outdir . "$PATH_DOW"
  rm ~/Downloads/"$P"

elif [[ $P == *.pdf ]]; then
  mv "$PATH_DOW" . 
fi

# Name=${P::-5}
# echo $Name
# mv "$Name".pdf .


