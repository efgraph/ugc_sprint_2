#!/bin/bash

echo "Waiting for API is OK"
python ./utils/api_check.py

pytest