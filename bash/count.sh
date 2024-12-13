#!/bin/bash

declare -A hash

while read word count; do
    let hash[$word]+=$count
done

for key in "${!hash[@]}"; do
    echo "word '$key' count = ${hash[$key]}"
done
