#!/bin/bash

source ~/tmp/envs/bin/activate
IPYNB_FILES=$(find . -name '*.ipynb' -not -path "./envs/*" -not -path "./.ipynb_checkpoints/*")
for f in $IPYNB_FILES
do
    jupyter nbconvert --to markdown $f
done