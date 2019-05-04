#!/bin/bash

NAME=$1

echo "Creating new page for $NAME..."

. ./scripts/html-template.sh | tee $NAME.html

echo "Created $NAME.html."
