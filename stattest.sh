#!/bin/sh

for f in "$@"
do
	stat $f
done