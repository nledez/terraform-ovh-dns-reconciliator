#!/bin/bash
./venv/bin/ptw --onpass "terminal-notifier -message '✅' -title 'Test OK'" --onfail "terminal-notifier -message '🔥' -title 'Test KO'"
