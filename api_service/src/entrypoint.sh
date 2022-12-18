#!/bin/sh

python3 /opt/app/src/wait-for-kafka.py

uvicorn main:app --host 0.0.0.0 --port 8000