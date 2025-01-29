# Define the Python interpreter and virtual environment directory
PYTHON = python3
VENV_DIR = venv

# Default target: Create virtual environment and install dependencies
all: venv install

# Create a virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies from requirements.txt
install: venv
	@echo "Activating virtual environment and installing dependencies..."
	. $(VENV_DIR)/bin/activate && pip install -r requirements.txt

.PHONY: all venv install
