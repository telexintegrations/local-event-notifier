## Local  Event Notifier
Local  Event Notifier built using FastAPI  Docker for containerization, Poetry for dependency management, and a Makefile for task automation.

### Features
- Fetches events based on city, and category.
- Docker for easy containerization and deployment.
- Poetry for managing dependencies and packaging.
- Pre-commit hooks for enforcing code quality and consistency before committing code.
- Sends events to Telex.

### Prerequisites
Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/)
- [Poetry ](https://python-poetry.org/)
- [Make](https://makefiletutorial.com/)
- [Pre-commit](https://pre-commit.com/)(for managing hooks) 

### Getting Started
Clone the repository
 ```shell
 git clone https://github.com/telexintegrations/local-event-notifier

 cd local-event-notifier
 ```
Create and activate a virtual environment: [install pyenv](https://github.com/pyenv/pyenv#installation)

#### Alternatively, using Python's built-in venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Set up dependencies with Poetry
Poetry is used for managing the Python dependencies. You can install them with:
 ```shell
 poetry install
 ```

### Install pre-commit hooks
Pre-commit hooks help enforce code quality before committing changes.
To install and configure pre-commit hooks:
1. Install pre-commit globally:
 ```shell
pip install pre-commit
 ```
2. Install the pre-commit hooks:
 ```shell
 pre-commit install
 ```
3. Run all hooks on all files (initial check):
 ```shell
 pre-commit run --all-files
 ```

### Pre-commit Hooks Overview
The following pre-commit hooks are configured for this project to ensure code quality:
- Code Style: Automatically formats code using black, sorts imports with isort, and checks for PEP 8 compliance with flake8.
- Code Quality: Verifies that docstrings are present, removes trailing whitespace, checks for correct Python syntax, and ensures logging is used correctly.
- Configuration Validation: Checks the correctness of TOML and YAML files, and ensures the Poetry configuration is set up properly.