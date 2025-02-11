@echo off
echo Setting up the Python project...

:: Step 1: Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python using the provided links and try again.
    exit /b 1
)

:: Step 2: Create a virtual environment
IF NOT EXIST "venv" (
    echo Creating a virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

:: Step 3: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 4: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Step 5: Install dependencies from requirements.txt
IF EXIST "requirements.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt not found! Skipping dependency installation.
)

echo Setup complete!
exit /b 0
