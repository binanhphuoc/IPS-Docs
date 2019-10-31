#!/bin/bash

pipenv shell
OUTPUT_DIR="."

while getopts ":o:" opt; do
  case ${opt} in
    o )
        OUTPUT_DIR=$OPTARG
      ;;
    \? ) 
        echo "Usage:"
        echo "  Opt       Default Argument    Description"
        echo "  [-o]      .                   output directory"
        echo "  [-h]      NONE                help"
        exit 0
      ;;
    : )
        echo "Invalid Option: -$OPTARG requires an argument" 1>&2
        exit 1
        ;;
  esac
done
shift $((OPTIND -1))

IPYNB_FILES=$(find . -name '*.ipynb' -not -path "./envs/*" -not -path "./.ipynb_checkpoints/*")
for f in $IPYNB_FILES
do
    # Replace "." with "$OUTPUT_DIR"
    output=${f/./$OUTPUT_DIR}
    # Get directory path of output
    output=$(dirname $output)
    echo $output
    # Convert files to folder $output
    jupyter nbconvert --output-dir=$output --to markdown $f
done