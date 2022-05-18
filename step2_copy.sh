#!/bin/bash

cd hellen-one
python3 ./bin/copy_from_Kicad.py "frames:hellen" ".." "../../gerber" "121vag" "c"

echo "Done!"
