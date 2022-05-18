#!/bin/bash

if [ ! -f "hellen-one/readme.md" ]; then
    echo "No submodule? Trying to pull"
    git submodule update --init --recursive
fi

cd hellen-one
sh bin/create_board_with_prefix.sh "hellen" ".." "121vag" "c" "bom_replace_121vag-c.csv" "80,0"
