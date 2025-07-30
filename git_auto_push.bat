@echo off
REM === Set your Git identity (first time only) ===
git config --global user.name "Edgar Pfuma"
git config --global user.email "cyber-engineer@outlook.com"

REM === Navigate to your automation folder ===
cd /d "%~dp0"

REM === Initialize git if needed ===
if not exist ".git" (
    git init
)

REM === Stage and commit changes ===
git add .
git commit -m "Auto commit by batch script"

REM === Set branch to main if not already set ===
git branch -M main

REM === Add remote if it doesn't exist ===
git remote | findstr origin >nul
if errorlevel 1 (
    git remote add origin https://github.com/cybergitengineer/Automation_Workflow.git
)

REM === Push to GitHub ===
git push -u origin main

pause
