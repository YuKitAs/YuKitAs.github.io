#!/bin/bash

for filename in ../*.html
do cp "$filename" "$filename.backup"
done
