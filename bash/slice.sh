#!/bin/bash


formater_text() {
    local text=$1
    local format=$2

    case $format in
    "l") echo ${text:0:1} ;;
    "r") echo ${text: -2} ;;
    "c") echo ${text:3:2} ;;
    "b") echo ${text:10:4} ;;
    "t") echo ${text:10} ;;
    esac
}

FN="/home/bin/util.sh"
echo "$(formater_text $FN "l")"
echo "$(formater_text $FN "r")"
echo "$(formater_text $FN "c")"
echo "$(formater_text $FN "b")"
echo "$(formater_text $FN "t")"

