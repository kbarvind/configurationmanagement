#!/bin/bash

cd ..

echo "Building project"

pip3.6 install -r requirements.txt

python3.6 setup.py sdist bdist_wheel

rm -rf build
