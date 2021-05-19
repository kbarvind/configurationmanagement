#!/bin/bash

cd ..

echo "Building project"

python3.7 setup.py sdist bdist_wheel

rm -rf build
