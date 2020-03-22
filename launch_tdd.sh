#!/bin/bash
source launch_config.sh

./venv/bin/ptw --onpass "terminal-notifier -message '✅' -title 'Test OK'" --onfail "terminal-notifier -message '🔥' -title 'Test KO'" -- $PYTEST_ARGS
