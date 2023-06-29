#!/bin/bash

# Заменить переменную в файле
filename="file.txt"
old_variable="[DOMAIN]"
new_variable="NEW_VALUE"

sed -i "s/$old_variable/$new_variable/g" "$filename"