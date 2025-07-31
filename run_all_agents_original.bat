@echo off

echo ======================================
echo AI Automation Suite - Run Agents
echo ======================================

cd /d "%~dp0"
set LOGFILE=agent_run_log.txt

echo ======== Run Log - %DATE% %TIME% ======== > %LOGFILE%
echo Logging output to %LOGFILE%

set /p runNews=Run News Agent? [Y/N]: 
set /p runStudy=Run Study Assistant? [Y/N]: 
set /p runJobs=Run Job Hunter? [Y/N]: 
set /p runClass=Run Class Summarizer? [Y/N]: 
set /p runProject=Run Project Builder? [Y/N]: 
set /p runBusiness=Run Business Research? [Y/N]: 

if /I "%runNews%"=="Y" (
    echo Running News Agent...
    echo [News Agent] ----------------------- >> %LOGFILE%
    python News_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runStudy%"=="Y" (
    echo Running Study Assistant Agent...
    echo [Study Assistant Agent] ----------- >> %LOGFILE%
    python Study_Assistant_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runJobs%"=="Y" (
    echo Running Job Hunter Agent...
    echo [Job Hunter Agent] ---------------- >> %LOGFILE%
    python Job_Hunter_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runClass%"=="Y" (
    echo Running Class Summarizer Agent...
    echo [Class Summarizer Agent] ---------- >> %LOGFILE%
    python Class_Summarizer_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runProject%"=="Y" (
    echo Running Project Builder Agent...
    echo [Project Builder Agent] ----------- >> %LOGFILE%
    python Project_Builder_Agent.py >> %LOGFILE% 2>&1
)

if /I "%runBusiness%"=="Y" (
    echo Running Business Research Agent...
    echo [Business Research Agent] --------- >> %LOGFILE%
    python Business_Research_Agent.py >> %LOGFILE% 2>&1
)

echo.
echo ======== Run Complete - %TIME% ======== >> %LOGFILE%
echo All selected agents completed. Output logged to: %LOGFILE%
pause
