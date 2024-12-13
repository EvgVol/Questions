#!/bin/bash


format_text() {
    local text=$1
    local format=$2

    case $format in 
        "uppercase")
            echo "${text^^}"
            ;;
        "lowercase")
            echo "${text,,}"
            ;;
        "capitalize")
            echo "${text^}"
            ;;
        *) echo "$text" ;;
    esac
}


text='hello world'
echo "Оригинальный текст: $text"
echo "${TXT^}: $(format_text "$text" "capitalize")"
echo "${TXT^^}: $(format_text "$text" "uppercase")"
echo "${TXT,}: $(format_text "Some Words" "capitalize")"
echo "${TXT,,}: $(format_text "Do Not YELL" "lowercase")"

