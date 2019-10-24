#!/bin/bash

MD_FILES=$(find . -name '*.md' -not -path "./envs/*" -not -path "./.ipynb_checkpoints/*")

factorial()
{
    MD_FILES=$(find $1 -maxdepth 1 -name '*.md' -type f)
    QUEUED_DIRS=$(find $1 -maxdepth 1 -type d -not -path "./.circleci | ./.git)" )
    echo $MD_FILES
    echo $QUEUED_DIRS
    # then
    #     echo 1
    # else
    #     last=$(factorial $[$1-1])
    #     echo $(($1 * last))
    # fi
}
factorial .