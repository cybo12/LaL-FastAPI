#!/bin/bash -ex

python -m pip install --no-cache-dir --upgrade -r ../application/requirements.txt
python -m pytest