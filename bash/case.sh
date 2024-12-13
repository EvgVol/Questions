#!/bin/bash

echo "Введите 'yes' или 'no'"
read answer


case $answer in
    yes)
        echo "Вы ввели yes"
        ;;
    no)
        echo "Вы ввели no"
        exit
        ;;
    *) echo "Попробуйте еще раз"
        ;;
esac
