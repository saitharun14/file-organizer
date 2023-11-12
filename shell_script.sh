#!/bin/bash

scriptDir=${0%/*}
scriptPath=$scriptDir"/script.py"
python3 $scriptPath $1 & disown