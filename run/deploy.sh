#!/bin/bash

cd ..

echo "copying artifacts"

cp -r dist/* ../PythonExecutables/boxconfig/


cd ../PythonExecutables

echo "Commiting to Git"

git add --all

git commit -m 'updated package'


echo "Pushing to git"
git push -u origin main


