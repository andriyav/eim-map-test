@echo off
echo Setting up the Python project...

:: Step 1: Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python using the provided links and try again.
    exit /b 1
)

:: Step 2: Clone the repository
SET /P REPO_URL="Enter the repository URL: "
IF NOT "%REPO_URL%"=="" (
    echo Cloning the repository...
    git clone %REPO_URL%
) ELSE (
    echo No repository URL provided. Skipping clone step.
)

:: Step 3: Change directory to the cloned repository
SET /P REPO_DIR="Enter the repository folder name: "
IF EXIST "%REPO_DIR%" (
    cd %REPO_DIR%
) ELSE (
    echo Repository folder not found! Make sure you entered the correct name.
    exit /b 1
)

:: Step 4: Create a virtual environment
IF NOT EXIST "venv" (
    echo Creating a virtual environment...
    python -m venv venv
) ELSE (
    echo Virtual environment already exists.
)

:: Step 5: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 6: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Step 7: Install dependencies from requirements.txt
IF EXIST "requirements.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt not found! Skipping dependency installation.
)

echo Setup complete!
exit /b 0
