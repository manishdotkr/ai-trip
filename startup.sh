#!/bin/bash

# Check if pip3 is installed, if not fall back to pip
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
else
    PIP_CMD="pip"
fi

# Check if pipenv is installed
if ! command -v pipenv &> /dev/null; then
    $PIP_CMD install pipenv
fi

# Check if Pipfile.lock is present
if [ ! -f "Pipfile.lock" ]; then
    pipenv install
fi

# Run the streamlit app
pipenv run streamlit run app.py
