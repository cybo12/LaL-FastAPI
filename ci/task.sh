#!/bin/bash -ex

python -m pip install uvicorn gunicorn fastapi fastapi-versioning pytest
python -m pytest