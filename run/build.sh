#!/bin/bash

cd ..

echo "Building project"

pip3.7 install -r requirements.txt

python3.7 setup.py sdist bdist_wheel bdist_egg

rm -rf build
