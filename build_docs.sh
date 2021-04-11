#!/bin/bash

rm -rf docs/_build

pip install --quiet -r requirements-docs.txt

make html

if [[ -z "${OPEN_BROWSER_AFTER_TEST}" ]]; then
  echo "Set OPEN_BROWSER_AFTER_TEST to open webbrowser w/ documentation after build"
else
  python -c "import os, webbrowser; webbrowser.open(f'file://{os.getcwd()}/docs/_build/html/index.html')"
fi
