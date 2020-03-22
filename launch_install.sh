#!/bin/bash
if [ "$1" = "dev" ]; then
	REQUIREMENTS="requirements.txt requirements-tests.txt requirements-dev.txt"
elif [ "$1" = "tests" ]; then
	REQUIREMENTS="requirements.txt requirements-tests.txt"
elif [ "$1" = "run" ]; then
	REQUIREMENTS="requirements.txt"
else
	REQUIREMENTS="requirements.txt"
fi
virtualenv -p $(which python3) venv
for f in $REQUIREMENTS; do
	./venv/bin/pip install -r $f
done
