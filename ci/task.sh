#!/bin/bash -ex

python -m pip install uvicorn gunicorn fastapi fastapi-versioning pytest httpx
python -m pytest