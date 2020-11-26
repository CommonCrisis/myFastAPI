[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# myFastAPI

Simple pre-config project for FastAPI

# Getting Started
Steps to run the backend locally:
1.	Install Python 3.7.x
2.  Install poetry [here](https://github.com/python-poetry/poetry#installation) \
    Linux: \
      `curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_PREVIEW=1 python` \
    Powershell:
    ```powershell
      Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py -OutFile get-poetry.py
      python .\get-poetry.py --preview
      Remove-Item .\get-poetry.py
      $env:Path += ";$env:USERPROFILE\.poetry\bin"
    ```
3.	Run the following commands:
    ```bash
    poetry shell
    poetry install
    poetry run task hooks
    ```
