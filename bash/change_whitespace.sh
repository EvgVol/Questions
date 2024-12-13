#!/bin/bash

change_whitespate() {
    local text=$1
    local format=$2

    case $format in
        "first")
            echo "${text/ /_}"
            ;;
        "all")
            echo "${text// /_}"
            ;;
        "without")
            echo "${text// /}"
            ;;
        "space")
            local str="${text/\//}"
            echo "${str//\// }"
            ;;
        fisrt-slash)
            echo "${text/\//}"
            ;;
    esac
}

text='Hello World super!'
text1="/usr/bin/filename"
echo "$(change_whitespate "$text" "first")"
echo "$(change_whitespate "$text" 'all')"
echo "$(change_whitespate "$text" 'without')"
echo "$(change_whitespate "$text1" 'space')"
echo "$(change_whitespate "$text1" 'fisrt-slash')"