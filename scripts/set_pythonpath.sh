#!/bin/bash
# According to this https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html
# 1. Add the module directory to PYTHONPATH
export PYTHONPATH="$PWD"
echo $PYTHONPATH
python scripts/script_a.py 

