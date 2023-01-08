#! /bin/bash

search_dir=input
rm input_files.txt
touch input_files.txt
for entry in "$search_dir"/*
do
  echo "$entry" >> input_files.txt
done