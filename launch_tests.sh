#!/bin/bash
source launch_config.sh

./venv/bin/pytest $PYTEST_ARGS
# --cov-config=.coveragerc
