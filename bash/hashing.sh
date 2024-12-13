#!/bin/bash


declare -A hash=( ["a"]=1 ["b"]=2 ["c"]=3 )

while read key value; do
    hash["$key"]="$value"
done

for k in "${!hash[@]}"; do
    echo "$k: ${hash[$k]}"
done

