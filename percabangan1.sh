#!/bin/bash

a=15
b=7

if [ $a == $b ]
then
  echo "a sama dengan b"
elif [ $a -gt $b ]
then 
  echo "a lebih besar dari b"
elif [ $a -lt $b ]
then
  echo "a leih kecil dari b"
else
  echo "Tidak ada kondisi yang memnuhi"
fi
