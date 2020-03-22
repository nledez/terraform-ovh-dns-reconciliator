#!/bin/bash
virtualenv -p $(which python3) venv
for f in requirements.txt requirements-tests.txt requirements-dev.txt; do
	./venv/bin/pip install -r $f
done
