@echo off

echo ======================================
echo AI Automation Suite - Run Agents
echo ======================================

cd /d "%~dp0"
set LOGFILE=agent_run_log.txt

REM === Create log file and add timestamp
echo ======== Run Log - %DATE% %TIME% ======== > %LOGFILE%
echo Log started. Selected agents will run below... >> %LOGFILE%
echo Logging output to %LOGFILE%

REM === Ask user whether to run all agents
set /p runAll=Do you want to run ALL agents? [Y/N]: 
if "%runAll%"=="" set runAll=N

REM === Ask individually if not all
if /I "%runAll:~0,1%"=="N" (
    echo.
    echo Select agents to run individually (Y/N):
    
    set /p runNews=Run News Agent? [Y/N]: 
    if "%runNews%"=="" set runNews=N

    set /p runStudy=Run Study Assistant? [Y/N]: 
    if "%runStudy%"=="" set runStudy=N

    set /p runJobs=Run Job Hunter? [Y/N]: 
    if "%runJobs%"=="" set runJobs=N

    set /p runClass=Run Class Summarizer? [Y/N]: 
    if "%runClass%"=="" set runClass=N

    set /p runProject=Run Project Builder? [Y/N]: 
    if "%runProject%"=="" set runProject=N

    set /p runBusiness=Run Business Research? [Y/N]: 
    if "%runBusiness%"=="" set runBusiness=N
)

REM === Force all to Y if runAll is Y
if /I "%runAll:~0,1%"=="Y" (
    set runNews=Y
    set runStudy=Y
    set runJobs=Y
    set runClass=Y
    set runProject=Y
    set runBusiness=Y
)

REM === Run selected agents
if /I "%runNews:~0,1%"=="Y" (
    echo Running News Agent...
    echo [News Agent] ----------------------- >> %LOGFILE%
    python News_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runStudy:~0,1%"=="Y" (
    echo Running Study Assistant Agent...
    echo [Study Assistant Agent] ----------- >> %LOGFILE%
    python Study_Assistant_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runJobs:~0,1%"=="Y" (
    echo Running Job Hunter Agent...
    echo [Job Hunter Agent] ---------------- >> %LOGFILE%
    python Job_Hunter_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runClass:~0,1%"=="Y" (
    echo Running Class Summarizer Agent...
    echo [Class Summarizer Agent] ---------- >> %LOGFILE%
    python Class_Summarizer_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runProject:~0,1%"=="Y" (
    echo Running Project Builder Agent...
    echo [Project Builder Agent] ----------- >> %LOGFILE%
    python Project_Builder_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runBusiness:~0,1%"=="Y" (
    echo Running Business Research Agent...
    echo [Business Research Agent] --------- >> %LOGFILE%
    python Business_Research_Agent.py >> %LOGFILE% 2>&1
)

echo. >> %LOGFILE%
echo ======== Run Complete - %TIME% ======== >> %LOGFILE%
echo All selected agents completed. Output logged to: %LOGFILE%
pause
