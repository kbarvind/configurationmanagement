#!/bin/bash

cd ..

echo "Executing project"

python3.7 app/cli/configmanagercli.py $@
