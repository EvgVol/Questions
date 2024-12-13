#!/bin/bash

if [ -z "$1" ]; then
    echo "Использование: $0 /путь/к/директории"
    exit 1
fi

cd "$1" || { echo "Не удалось перейти в директорию: $1"; exit 1; }

for file in *.jpeg; do
    mv -v "$file" "${file/jpeg/jpg}";
    # if [ -e "$file" ]; then
    #     echo mv -v "$file" "$*.{file/JPEG/jpg}.jpg"
    # fi
done